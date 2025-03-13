import pandas as pd
# Original dataframe
df = pd.DataFrame({
    'name': ['zhangsan', 'lisi', 'wangwu', 'zhaoliu'],
    'age': [20, 30, 25, 35],
    'city': ['qingdao', 'shijiazhuang', 'zhengzhou', 'taiyuan'],
    'province' : ['shandong', 'hebei', 'henan', 'shanxi'],
    'Location': ['qingdao,shandong', 'shijiazhuang,hebei', 'zhengzhou, henan', 'taiyuan, shanxi']
}, index=['1', '2', '3', '4'])

# print(df, "\n")

# Splitting Columns
location_split = df['Location'].str.split(
    pat=',', # use comma as the delimiter
    expand=True # The expand parameter with the True argument returns a DataFrame with the strings split into columns
)
# 现在的location_split是一个表格, 见这个课程https://www.codecademy.com/courses/getting-started-with-python-for-data-science/lessons/cleaning-and-transforming-columns/exercises/splitting-and-combining-columns
# 已经通过, 分隔开成两列了
'''
   0        1
qingdao shandong
shijiazhuang hebei
zhengzhou henan
taiyuan shanxi
'''

# assign a non-existing column, say named place
df['place'] = location_split[0]
print(df.head())

# Combing Columns
# 通过空格连接city和province两列
df['combine_location'] = df['city'].str.cat(df['province'], sep=' ')
print(df[['city', 'province', 'combine_location']])