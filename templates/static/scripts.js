document.addEventListener('DOMContentLoaded', function () {
    // 获取所有图例按钮
    const legendButtons = document.querySelectorAll('.legend-item');

    // 获取地图图片元素
    const mapImage = document.getElementById('map-image');

    // 给每个图例按钮添加点击事件监听器
    legendButtons.forEach(button => {
        button.addEventListener('click', function () {
            // 获取点击的按钮的类名
            const className = button.querySelector('.legend-text').textContent;; // 第二个类名是按钮的唯一标识
            console.log(className)
            // 根据按钮类名切换地图图片
            switch (className) {
                case '站点位置':
                    mapImage.src = '/static/station.png';
                    break;
                case '一号线':
                    mapImage.src = '/static/line1.png';
                    break;
                case '二号线':
                    mapImage.src = '/static/line2.png';
                    break;
                case '三号线':
                    mapImage.src = '/static/line3.png';
                    break;
                case '四号线':
                    mapImage.src = '/static/line4.png';
                    break;
                case "坐标系":
                    mapImage.src = '/static/image_with_label.png';
                    break;
                default:
                    mapImage.src = '/static/image.png';
            }
        });
    });
});

