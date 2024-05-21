"""
演示循环语句的中断控制：break和continue
"""

# 演示循环中断语句 continue
# 用于根据某些条件跳过当前循环的剩余部分
for i in range(1, 6):
    print("语句1")
    continue
    print("语句2")

# 演示continue的嵌套应用
for i in range(1, 6):
    print("语句1")
    for j in range(1, 6):
        print("语句2")
        continue
        print("语句3")

    print("语句4")

# 示例一
# 使用continue打印奇数
current_number = 0
while current_number < 10:
    current_number += 1
    if (current_number % 2) == 0:
        continue
    print(current_number)


