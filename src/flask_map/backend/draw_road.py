from flask_map.myutils import project_path
from flask_map.backend.Coordinate import line1, line2, line3, line4
import os
from PIL import ImageDraw, Image
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib.image as mpimg


image_path = os.path.join(project_path, "templates", "static")
image_name = os.path.join(image_path, "image.png")
font_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "SourceHanSansSC-Regular.otf"
)  # 替换为你的中文字体路径
prop = FontProperties(fname=font_path)

plt.switch_backend("agg")


def draw_road(coords, title, color):
    # 读取地图图像
    image = Image.open(image_name)
    map_img = ImageDraw.Draw(image)
    point = []
    for i in range(len(coords)):
        point.append([coords[i].x, coords[i].y])
    point_array = np.array(point)
    # 依次连接每个点形成线
    for i in range(len(point) - 1):
        point1 = tuple(point_array[i])
        point2 = tuple(point_array[i + 1])
        map_img.line([point1, point2], fill=color, width=25)

    fig, ax = plt.subplots()
    ax.imshow(image)
    temp_dir = os.path.join(project_path, "templates", "static", "temp.png")
    image.save(temp_dir)

    map_img = mpimg.imread(temp_dir)

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

    dst_name = f"{title}.png"
    dst_dir = os.path.join(image_path, dst_name)
    plt.savefig(
        dst_dir, dpi=map_img.shape[1] / fig.get_size_inches()[0], bbox_inches="tight"
    )


if __name__ == "__main__":
    draw_road(line1.coordinates, "line1", "green")
    draw_road(line2.coordinates, "line2", "blue")
    draw_road(line3.coordinates, "line3", "yellow")
    draw_road(line4.coordinates, "line4", "purple")
