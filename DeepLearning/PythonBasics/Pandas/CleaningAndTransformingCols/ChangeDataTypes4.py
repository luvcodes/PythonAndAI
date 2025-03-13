import pandas as pd
# Original dataframe
df = pd.DataFrame({
    'name': ['zhangsan', 'lisi', 'wangwu', 'zhaoliu'],
    'age': [20, 30, 25, 35],
    'city': ['qingdao', 'shijiazhuang', 'zhengzhou', 'taiyuan'],
    'province' : ['shandong ', 'hebei ', 'henan ', 'shanxi '],
    'code': ['1', '2', '3', '4']
}, index=['1', '2', '3', '4'])

# Change data type
print(df.info())
df['code'] = df['code'].astype('int64')
print(df.info())
