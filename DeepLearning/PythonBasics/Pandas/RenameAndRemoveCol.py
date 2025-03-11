import pandas as pd
# Original dataframe
df = pd.DataFrame({
    'name': ['zhangsan', 'lisi', 'wangwu', 'zhaoliu'],
    'age': [20, 30, 25, 35],
    'city': ['beijing', 'shanghai', 'guangzhou', 'shenzhen']
}, index=['1', '2', '3', '4'])

print(df, "\n")

# Rename columns using the column mappers
column_mappers = {
    'name':'name1',
    'age':'age1',
    'city':'city1',
}

df = df.rename(
    mapper=column_mappers,
    axis=1 # 1 means col, 0 means row
)

print(df, "\n")


# drop columns
drop_columns = {'city1'}
df = df.drop(
    labels=drop_columns,
    axis=1
)
print(df, "\n")