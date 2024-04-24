import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from flask_map.backend.Coordinate import Coordinate, location_dic
from matplotlib.font_manager import FontProperties
from flask_map.myutils import project_path
import os
from adjustText import adjust_text

font_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "SourceHanSansSC-Regular.otf"
)  # 替换为你的中文字体路径
prop = FontProperties(fname=font_path)

plt.switch_backend("agg")


def show_coordinate_on_map(coordinates, dst_name):
    """
    显示指定坐标在地图图像上的位置。
    """
    image_path = os.path.join(project_path, "templates", "static")
    image_name = os.path.join(image_path, "image.png")
    # 读取地图图像
    map_img = mpimg.imread(image_name)

    # 创建图像和坐标轴对象
    fig, ax = plt.subplots()
    ax.imshow(map_img)

    # 设置坐标轴范围，根据地图的实际坐标范围来设置
    ax.set_xlim(0, map_img.shape[1])
    ax.set_ylim(map_img.shape[0], 0)

    # 将 X 轴和 Y 轴的刻度也显示在图像上方和右侧，并设置字体大小
    ax.xaxis.tick_top()
    plt.xticks(fontsize=3)
    plt.yticks(fontsize=3)
    for station in coordinates:
        # 标记指定的坐标
        if "公交" in station:
            color = "blue"
            co = "b*"
        else:
            color = "red"
            co = "ro"
        ax.plot(
            coordinates[station].x, coordinates[station].y, co, markersize=2
        )  # 'ro'表示红色圆点，markersize为标记大小
        # 在标记点旁边添加标签
        if (
            station == "振声苑站4"
            or station == "地铁山东大学站"
            or station == "乐水居步行街西口站"
            or station == "阅海居站"
        ):
            xytext = (0, -5)
        else:
            xytext = (0, 5)
        ax.annotate(
            station,
            xy=[coordinates[station].x, coordinates[station].y],
            xytext=xytext,
            textcoords="offset points",
            ha="center",
            va="center",
            fontsize=4,
            color=color,
            weight="bold",
            fontproperties=prop,
        )

    dst_dir = os.path.join(image_path, dst_name)
    # plt.axis("off")  # 关闭坐标轴
    plt.savefig(
        dst_dir, dpi=map_img.shape[1] / fig.get_size_inches()[0], bbox_inches="tight"
    )


if __name__ == "__main__":
    show_coordinate_on_map(location_dic, "station_no.png")
