from flask import Flask, render_template, request, redirect, jsonify
import os
from flask_map.myutils import project_path
from flask_map.backend.show_coordinate import show_coordinate_on_map
from flask_map.backend.Coordinate import (
    Coordinate,
    line4,
    line1,
    line2,
    line3,
    get_coord,
    get_time_list,
    location_dic,
    out_distance,
)
from flask_map.myutils.config import config
import shutil

template_folder = os.path.join(project_path, "templates")
static_folder = os.path.join(template_folder, "static")

app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)

# 公交车满载人数
num = int(config["bus"]["num"])
speed = config["bus"]["speed"]

# 统计当前的公交车
bus_list = []


@app.route("/", methods=["GET"])
def index():
    """
    首页，显示初始界面
    """
    # 渲染初始页面模板
    if request.method == "GET":
        image_filename = "station.png"
        return render_template("index.html", image_filename=image_filename)


@app.route("/location/", methods=["GET"])
def location():
    """
    用户提交位置后显示自己的位置和最近公交车站位置
    """
    if request.method == "GET":
        user_x = request.args.get("user-x", "")
        user_y = request.args.get("user-y", "")
        try:
            if (
                int(user_x) < 0
                or int(user_x) > 2800
                or int(user_y) < 0
                or int(user_y) > 5000
            ):
                return '<script> alert("x坐标在0~2800之间，y坐标在0~5000之间");window.history.back();</script>'

            my_location = Coordinate(int(user_x), int(user_y))
            min_distance = 999999
            min_bus_station = None

            for station in location_dic:
                distance = my_location.distance_to(location_dic[station])
                if distance < min_distance:
                    min_bus_station = station
                    min_distance = distance

            image_filename = "my_location.png"
            show_coordinate_on_map(
                {
                    "my_location": my_location,
                    min_bus_station: location_dic[min_bus_station],
                },
                image_filename,
            )

            return render_template(
                "location.html",
                image_filename=image_filename,
                key=min_bus_station,
                value=str(int(min_distance)),
                coor=f"({int(location_dic[min_bus_station].x)}, {int(location_dic[min_bus_station].y)})",
                my_coor=f"({my_location.x}, {my_location.y})",
            )

        except ValueError:
            return (
                '<script> alert("传输的值必须为数字");window.history.back();</script>'
            )


@app.route("/bus/", methods=["POST", "GET"])
def bus():
    """
    处理公交车信息
    """
    if request.method == "GET":
        bus_distance = request.args.get("bus-distance", "")
        line = request.args.get("bus-line", "")
        passengers = request.args.get("bus-passengers", "")

        if bus_distance and line and passengers:
            try:
                bus_distance = int(bus_distance)
                passengers = int(passengers)

                if passengers > num:
                    return '<script> alert("车内人员已经满载");window.history.back();</script>'

                if out_distance(line, bus_distance):
                    return '<script> alert("公交车距离起始站已超过最大距离");window.history.back();</script>'

                bus_coord = get_coord(line, bus_distance)

                if passengers > num * 0.8:
                    yongji = "拥挤"
                elif passengers > num * 0.5:
                    yongji = "正常"
                else:
                    yongji = "轻松"
                flag = 0
                for i in range(len(bus_list)):
                    if (
                        bus_distance == bus_list[i]["distance"]
                        and line == bus_list[i]["line"]
                    ):
                        flag = 1
                        break
                if flag == 0:
                    bus_list.append(
                        {
                            "bus_coord": bus_coord,
                            "line": line,
                            "yongji": yongji,
                            "distance": bus_distance,
                            "shengyu": num - passengers,
                        }
                    )

                image_filename = "bus.png"
                map_dic = {}

                for i in range(0, len(bus_list)):
                    map_dic[f"公交{str(i+1)}"] = bus_list[i]["bus_coord"]
                    bus_list[i]["name"] = f"公交{str(i+1)}"

                show_coordinate_on_map(map_dic, image_filename)

                return render_template(
                    "bus.html", image_filename=image_filename, global_list=bus_list
                )

            except ValueError:
                return '<script> alert("传输的值必须为数字");window.history.back();</script>'

        else:
            image_filename = "bus.png"
            return render_template(
                "bus.html", image_filename=image_filename, global_list=bus_list
            )


@app.route("/clear_buses", methods=["POST"])
def clear_buses():
    """
    清空公交车信息
    """
    global bus_list
    bus_list = []  # 清空公交车列表
    src_image = os.path.join(
        project_path, "templates", "static", "image_with_label.png"
    )
    dst_image = os.path.join(project_path, "templates", "static", "bus.png")
    shutil.copy(src_image, dst_image)
    return redirect("/bus/")  # 重定向回首页


@app.route("/bus_detail", methods=["GET"])
def bus_detail():
    """
    公交车到站详情
    """
    station_list = []
    bus_name = request.args.get("bus-name", "")
    time_list = []

    for i in range(0, len(bus_list)):
        if bus_list[i]["name"] == bus_name:
            time_list = get_time_list(bus_list[i]["line"], bus_list[i]["distance"])
            shengyu = bus_list[i]["shengyu"]
            break

    for i in range(0, len(time_list)):
        for j in location_dic:
            if (
                location_dic[j].x == time_list[i][0].x
                and location_dic[j].y == time_list[i][0].y
            ):
                station_list.append(f"{j} : {str(time_list[i][1])}")
                break

    station = "<br>".join(station_list)

    response_data = {
        "message": f"当前速度：{speed}<br><br>{bus_name} 到各站的时间：<br>{station}<br><br>该公交车剩余座位：{shengyu}"
    }
    return jsonify(response_data)


@app.route("/button")
def button():
    return render_template("test.html")


@app.route("/button_clicked", methods=["POST"])
def button_clicked():
    # 处理按钮点击的逻辑
    # 可以在这里执行一些操作，比如调用其他函数或处理数据

    # 返回数据给前端，这里假设返回一个简单的 JSON
    response_data = {"message": "按钮被点击了！"}
    return jsonify(response_data)


if __name__ == "__main__":
    app.run(debug=True)
