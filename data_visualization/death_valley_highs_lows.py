import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'death_valley_2018_simple.csv'
with open(filename) as file:
    reader = csv.reader(file)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

        # 提取并读取数据
        # 从文件中获取最高、低温度和日期
    highs, lows, dates = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f'Missing data for {current_date}')
        else:
            highs.append(high)
            lows.append(low)
            dates.append(current_date)

# 绘制温度曲线,alpha代表透明度
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置图形格式
title = '2018 day of tmax & tmin\n USA'
ax.set_title(title, fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('temp(F)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
