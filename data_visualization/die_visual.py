from die import Die

# 创建一个D6骰子
die = Die()

# 投掷几次骰子并将结果存储在列表中
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

print(results)