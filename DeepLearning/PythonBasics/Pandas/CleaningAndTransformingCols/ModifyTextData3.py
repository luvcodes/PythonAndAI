import pandas as pd


# Original dataframe
df = pd.DataFrame({
    'name': ['zhangsan', 'lisi', 'wangwu', 'zhaoliu'],
    'age': [20, 30, 25, 35],
    'city': ['qingdao', 'shijiazhuang', 'zhengzhou', 'taiyuan'],
    'province' : ['shandong ', 'hebei ', 'henan ', 'shanxi '],
    'Location': ['qingdao,shandong', 'shijiazhuang,hebei', 'zhengzhou,henan', 'taiyuan,shanxi']
}, index=['1', '2', '3', '4'])

# 修改大小写 upper lower title
# 想要把city中的所有元素都改成首字母大写
df['city'] = df['city'].str.title()
print(df.head())

# 去除元素中的空格 strip
# 想要去除province中的所有元素的空格
df['province'] = df['province'].str.strip()
print(df.head())

# 替换元素中的内容
# 想要把Location中的所有,都改成空格
df['Location'] = df['Location'].str.replace(pat=',', repl=' ', regex=False)
print(df.head())