import matplotlib.pyplot as plt

# 自动计算值
input_values = range(1, 1001)
squares = [x**2 for x in input_values]

# 添加样式
plt.style.use('seaborn')

fig, ax = plt.subplots()
# 绘制散点图,s：点的大小,c：点的颜色，也可以用（0, 0.8, 0），也可以映射cmap对应的颜色
ax.scatter(input_values, squares, s=100, c=squares, cmap=plt.cm.Blues)
# 绘制折线图
# 修改线条粗细
ax.plot(input_values, squares, linewidth=2)
# 设置标签文字和,图表标题并给坐标轴加标签
ax.set_title("ping_fang_shu", fontsize=24)
ax.set_xlabel("value", fontsize=14)
ax.set_ylabel("value_ping_fang", fontsize=14)
# 设置刻度标记的大小
ax.tick_params(axis='both', labelsize=14)
# 设置每个坐标轴的取值范围
ax.axis([0, 1100, 0, 1100000])

# 展示图表
plt.show()
# 自动保存图表,bbox_inches='tight'表示减掉多余的空白区
# plt.savefig('a.png')

