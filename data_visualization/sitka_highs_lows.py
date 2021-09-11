import csv
from datetime import datetime

import matplotlib.pyplot as plt


file_name = 'sitka_weather_2018_simple.csv'
with open(file_name) as file:
    reader = csv.reader(file)
    header_row = next(reader)
    print(header_row)
    # 打开文件头及其位置
    for index, colnum_header in enumerate(header_row):
        print(index, colnum_header)

    # 提取并读取数据
    # 从文件中获取最高、低温度和日期
    highs, lows, dates = [], [], []
    for row in reader:
        high = int(row[5])
        highs.append(high)
        low = int(row[6])
        lows.append(low)
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)

    print(highs)

# 绘制温度曲线,alpha代表透明度
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)


# 设置图形格式
ax.set_title('2018,day_max_temp', fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('temp(F)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
