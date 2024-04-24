# 山东大学公交车管理系统

主要实现三个功能：
1. 通过按键切换显示原图、站点位置、一号线到四号线
2. 手动输入本人位置坐标，可在地图上显示出本人的位置，并显示最近的公交站点和位置
3. 手动输入公交车的位置、所在线路和公交车人数，可在地图上显示公交车当前所在位置，并预计到线路中后序站点的时间，还有此时车厢拥挤情况

## 目录结构

```
├── README.md               # 项目说明文件
├── config                  # 配置文件目录
│   └── config.ini          # 配置文件
├── data                    # 数据存储目录
├── logs                    # 日志文件目录
│   └── default.log         # 默认日志文件
├── src                     # 源代码目录
│   └── flask_map           
│       ├── __init__.py
│       ├── __pycache__
│       │   └── ...
│       ├── backend         # 后端代码目录
│       │   ├── Coordinate.py           # 坐标类和线路类
│       │   ├── SourceHanSansSC-Regular.otf   # 字体文件
│       │   ├── __pycache__
│       │   │   └── ...
│       │   ├── app.py          # Flask应用入口
│       │   ├── get_coordinate_from_input.py    # 交互式获得坐标
│       │   ├── show_coordinate.py             # 在地图上绘制坐标点
│       │   └── show_coordinate_map.py        # 绘制带坐标轴的地图
│       └── myutils         # 自定义工具类目录
│           ├── __init__.py
│           ├── __pycache__
│           │   └── ...
│           ├── config.py       # 配置工具
│           └── logger.py       # 日志工具
└── templates               # Flask模板目录
    ├── bus.html            # 公交车信息模板
    ├── index.html          # 首页模板
    ├── location.html       # 位置信息模板
    └── static              # 静态文件目录
        ├── bus.png                 # 公交车信息图
        ├── image.png               # 原图示例
        ├── image_with_label.png    
        ├── line1.png               # 线路1
        ├── line2.png               # 线路2
        ├── line3.png               # 线路3
        ├── line4.png               # 线路4
        ├── my_location.png         # 带我的位置坐标
        ├── origin_image.png        # 原始图片
        ├── scripts.js              # JavaScript脚本
        ├── station.png             # 各站点图片
        └── styles.css              # CSS样式表
```

## 快速开始
1. 安装依赖
```
pip install -r requirements.txt
```

2. 运行应用
```
cd src
python -m flask_map.backend.app
```