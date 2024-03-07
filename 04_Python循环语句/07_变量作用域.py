"""
演示Python for循环临时变量的作用域
"""

i = 0
for i in range(5):
    print(i)

# 这里就是体现，最后的i的值就是4。
# 没有增加到5
print(i)

