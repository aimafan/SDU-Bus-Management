# 交互式的获得某点坐标，主要用来计算站点坐标

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from flask_map.myutils import project_path
import os


image_path = os.path.join(project_path, "templates", "static", "image.png")
# 读取图像
image = plt.imread(image_path)


# 读取地图图像
map_img = mpimg.imread(image_path)

# 创建图像和坐标轴对象
fig, ax = plt.subplots()
ax.imshow(map_img)

# 添加坐标轴标签
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')

# 设置坐标轴范围，根据地图的实际坐标范围来设置
ax.set_xlim(0, map_img.shape[1])
ax.set_ylim(map_img.shape[0], 0)

# 将 X 轴和 Y 轴的刻度显示在图像上方和右侧
ax.xaxis.set_label_position('top')
ax.yaxis.set_label_position('right')

# 将 X 轴和 Y 轴的刻度也显示在图像上方和右侧，并设置字体大小
ax.xaxis.tick_top()
ax.yaxis.tick_right()
plt.xticks(fontsize=4)
plt.yticks(fontsize=4)

while(True):
    # 交互式获取坐标
    coords = plt.ginput(n=1, timeout=0)

    # 打印点击的坐标
    if coords:
        clicked_x, clicked_y = coords[0]
        print(f"Clicked Coordinates: ({clicked_x}, {clicked_y})")
