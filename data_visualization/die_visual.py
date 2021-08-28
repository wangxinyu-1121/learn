from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# 创建两个不同的骰子
die_1 = Die()
die_2 = Die(8)

# 投掷几次骰子并将结果存储在列表中
results = []
for roll_num in range(5000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(results)
print(frequencies)
# 对结果进行可视化
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]
# dtick指定了x轴显示的刻度间距
x_axis_config = {'title': '结果', 'dtick': 1}
y_axis_config = {'title': '结果频次'}
my_layout = Layout(title='投5000次1个D6和一个D8骰子的结果', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d8.html')

