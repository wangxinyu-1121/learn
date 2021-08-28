import matplotlib.pyplot as plt
from random_walk import RandomWalk

# 只要程序处于活动状态，就不断的模拟随机漫步
while True:
    # 创建一个RandWalk实例
    rw = RandomWalk(50_000)
    rw.fill_walk()
    # 将所有的点都绘制出来
    plt.style.use('classic')
    # 调整图表尺寸和分辨率
    fig, ax = plt.subplots(figsize=(15, 9), dpi=128)
    point_numbers = range(rw.num_points)
    # edgecolor表示删除轮廓颜色
    ax.scatter(rw.x_values, rw.y_values, s=1, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none')
    # 突出起点和终点
    ax.scatter(0, 0, c='green', edgecolors='none', s=50)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=50)
    # 隐藏坐标轴
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input('make another walk?(Y/N)')
    if keep_running in ('n', 'N', 'no', 'NO', 'No', 'no'):
        break
