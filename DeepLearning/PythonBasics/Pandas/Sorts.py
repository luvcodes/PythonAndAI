import pandas as pd
# Original dataframe
df = pd.DataFrame({
    'name': ['zhangsan', 'lisi', 'wangwu', 'zhaoliu'],
    'age': [20, 30, 25, 35],
    'city': ['beijing', 'shanghai', 'guangzhou', 'shenzhen']
}, index=['a', 'b', 'c', 'd'])

print(df, "\n")

# 排序sorting
df = df.sort_values('age', ascending=False)
print(df)