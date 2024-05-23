"""
演示对文件的读取
"""

# 打开文件
import time
from pathlib import Path


# # 通过Path来读取txt文件中的文本内容
# path = Path('测试.txt')
# # 直接这样读取会在结果中显示出来一个空行
# contents = path.read_text()
# # 想要去掉这个空行可以使用rstrip()方法
# contents = contents.rstrip()
# print(contents)

# 访问文件中的各行
# path = Path('测试.txt')
# contents = path.read_text()
# lines = contents.splitlines()
# for line in lines:
#     print(line)


# 使用文件中的内容
path = Path('测试.txt')
contents = path.read_text()
lines = contents.splitlines()
textStr = ''
for line in lines:
    textStr += line
print(textStr)
print(len(textStr))




# f = open(r"测试.txt", "r", encoding="UTF-8")
# print(type(f))
# 读取文件 - read()
# print(f"读取10个字节的结果：{f.read(10)}")
# print(f"read方法读取全部内容的结果是：{f.read()}")
# print("-----------------------------------------------")

# 读取文件 - readLines() 读取文件的全部行，封装到列表中
# lines = f.readlines()
# print(f"lines对象的类型：{type(lines)}")
# print(f"lines对象的内容是：{lines}")

# 读取文件 - readline()
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(f"第一行数据是：{line1}")
# print(f"第二行数据是：{line2}")
# print(f"第三行数据是：{line3}")

# for循环读取文件行
# for line in f:
#     print(f"每一行数据是:{line}")

# # 文件的关闭
# f.close()
# time.sleep(500000)

# with open 语法操作文件
# with open("测试.txt", "r", encoding="UTF-8") as f:
#     for line in f:
#         print(f"每一行数据是：{line}")
#
# time.sleep(500000)
