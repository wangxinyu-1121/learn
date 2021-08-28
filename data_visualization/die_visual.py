from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# 创建一个D6骰子
die = Die()

# 投掷几次骰子并将结果存储在列表中
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# 分析结果
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(results)
print(frequencies)
# 对结果进行可视化
x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': '结果'}
y_axis_config = {'title': '结果频次'}
my_layout = Layout(title='投1000次D6骰子的结果', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')

