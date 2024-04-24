# 打印携带坐标轴的地图
import matplotlib.pyplot as plt
from flask_map.myutils import project_path
import os


image_path = os.path.join(project_path, "templates", "static")
image_name = os.path.join(image_path, "image.png")
# 读取图像
image = plt.imread(image_name) 
# 创建图像和坐标轴对象
fig, ax = plt.subplots()
ax.imshow(image)



# 设置坐标轴范围，根据地图的实际坐标范围来设置
ax.set_xlim(0, image.shape[1])
ax.set_ylim(image.shape[0], 0)

# 将 X 轴显示在图像上方
ax.xaxis.set_label_position('top')
ax.xaxis.tick_top()
plt.xticks(fontsize=3)
plt.yticks(fontsize=3)

dst_dir = os.path.join(image_path, "image_with_label.png")
plt.savefig(dst_dir, dpi=image.shape[1]/fig.get_size_inches()[0], bbox_inches='tight')