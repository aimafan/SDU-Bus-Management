# 山东大学公交车管理系统

## 基本功能介绍

主要实现三个功能：
1. 通过按键切换显示原图、站点位置、一号线到四号线
2. 手动输入本人位置坐标，可在地图上显示出本人的位置，并显示最近的公交站点和位置
3. 手动输入公交车的位置、所在线路和公交车人数，可在地图上显示公交车当前所在位置，并预计到线路中后序站点的时间，还有此时车厢拥挤情况


## 快速开始

1. 克隆仓库
```
git clone http://github.com/aimafan/SDU-Bus-Management
```

2. 安装依赖
```
pip install -r requirements.txt
```

3. 运行应用
```
cd src
python -m flask_map.backend.app
```

## 运行截图

[](https://image.aimafan.top/blog/202404241936636.png)

[](https://image.aimafan.top/blog/202404241936392.png)

[](https://image.aimafan.top/blog/202404241937300.png)
