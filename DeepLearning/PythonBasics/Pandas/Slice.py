import pandas as pd
# Original dataframe
df = pd.DataFrame({
    'name': ['zhangsan', 'lisi', 'wangwu', 'zhaoliu'],
    'age': [20, 30, 25, 35],
    'city': ['beijing', 'shanghai', 'guangzhou', 'shenzhen']
}, index=['1', '2', '3', '4'])

print(df, "\n")

'''
✅ 何时用 loc[]？
当 索引是自定义标签 时（如 'a', 'b', 'c'）。
选取特定行名或列名时。
✅ 何时用 iloc[]？
当你需要 基于行号/列号选取数据。
数据是默认整数索引时（0,1,2,…）。
'''

# loc[]方法 基于标签的索引
# 使用行索引获取数据
print(df.loc['2'], "\n")
# 使用多个行索引获取数据
print(df.loc[['2', '3']], "\n")
# 使用列索引获取数据
print(df.loc[:, 'name'], "\n")
# 使用多个列索引获取数据
print(df.loc[:, ['name', 'age']], "\n")
# 行切片, 闭区间，包括3
print(df.loc['1':'3'], "\n")
print(df.loc['1':'3', ['name', 'age']], "\n")
# loc[]条件筛选
print(df.loc[df['age'] > 25])

# iloc[]方法 基于整数位置的索引
'''
df.iloc[行号, 列号] 
切片是 左闭右开（即 end 不包含）
'''
# iloc[]选取单行
print(df.iloc[1], "\n")
# iloc[]选取多行
print(df.iloc[[1,2]], "\n")
# iloc[]选取单列
print(df.iloc[:, 1], "\n")
# iloc[]选取多列
print(df.iloc[:, [0, 2]], "\n")
# iloc[]行切片
print(df.iloc[0:3], "\n")