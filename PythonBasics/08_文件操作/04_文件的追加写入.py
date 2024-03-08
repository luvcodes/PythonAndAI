"""
演示文件的追加写入
"""

# 打开文件，不存在的文件
f = open(r"C:\Users\ryanw\OneDrive\Desktop\PythonAndAI\PythonBasics\08_文件操作\测试.txt", "a", encoding="UTF-8")
# write写入
f.write("黑马程序员")
# flush刷新
f.flush()
# close关闭
f.close()

# # 打开一个存在的文件
# f = open(r"C:\Users\ryanw\OneDrive\Desktop\PythonAndAI\PythonBasics\08_文件操作\测试.txt", "r", encoding="UTF-8")
#
# # write写入、flush刷新
# f.write("\n月薪过万")

# # 打开一个存在的文件以追加内容
# with open(r"C:\Users\ryanw\OneDrive\Desktop\PythonAndAI\PythonBasics\08_文件操作\测试.txt", "a", encoding="UTF-8") as f:
#     # write写入、flush刷新
#     f.write("\n月薪过万")
#     # with语句块结束时，文件自动关闭

# close关闭
f.close()
