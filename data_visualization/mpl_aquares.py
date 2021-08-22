#!/usr/bin/python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5, ]
squares = [1, 4, 9, 16, 25, ]
fig, ax = plt.subplots()
# 修改标签文字和线条粗细
ax.plot(input_values, squares, linewidth=2)
# 设置图表标题并给坐标轴加标签
ax.set_title("ping_fang_shu", fontsize=24)
ax.set_xlabel("value", fontsize=14)
ax.set_ylabel("value_ping_fang", fontsize=14)

# 设置刻度标记的大小
ax.tick_params(axis='both', labelsize=14)

# 展示图表
plt.show()
