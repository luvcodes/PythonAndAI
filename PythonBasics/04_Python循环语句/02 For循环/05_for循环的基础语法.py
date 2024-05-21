"""
演示for循环的基础语法
"""

name = "itheima"

for x in name:
    # 将name的内容，挨个取出赋予x临时变量
    # 就可以在循环体内对x进行处理
    print(x)

nameList = ['itheima', 'python', 'Java']
for name in nameList:
    print(f"Name: {name.title()}, that was a good name!")

"""
演示for循环的练习题：数一数有几个a
"""
# 统计如下字符串中，有多少个字母a
name = "itheima is a brand of itcast"
count = 0
for x in name:
    if x == "a":
        count += 1

print(f"被统计的字符串中有{count}个a")


