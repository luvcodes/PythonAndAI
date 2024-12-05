# 通过%的方式，格式化输出
# 第一种: 通过%s的方式，格式化string类型
name = "Python"
print("Hello %s" % name)
# 第二种: 通过%d的方式，格式化int类型
age = 23
print("I'm %d years old" % age)
age2 = 23.2323
print("I'm %.2f years old" % age2)
# 第三种：通过%f的方式，格式化float类型
currentTime = 16.4603
print("Current time is %f " % currentTime)
print("宽度限制：%5d" % 10)  # 输出：宽度限制：   10
print("小数精度：%7.2f" % 3.14159)  # 输出：小数精度：   3.14
print("左对齐：%-5d" % 10)  # 输出：左对齐：10
print("-------------------------")

# 使用str.format()方式来格式化字符串
print("Hello, {}!".format("Alice"))  # 输出：Hello, Alice!
# print("整数：{0}, 浮点数：{1:.2f}".format(10, 3.14159))  # 输出：整数：10, 浮点数：3.14
print("浮点数: {1:.1f}, 整数: {0}".format(10, 3.14159))  # 输出：浮点数: 3.1, 整数: 10
print("姓名：{name}, 年龄：{age}".format(name="Alice", age=25))  # 输出：姓名：Alice, 年龄：25
print("左对齐：{:<5}".format(10))  # 输出：左对齐：10
print("小数精度：{:.2f}".format(3.14159))  # 输出：小数精度：3.14
print("宽度和精度：{:<7.2f}".format(3.14159))  # 输出：宽度和精度：3.14
print("-------------------------")

# 使用f-string的方式来格式化字符串
name = "Alice"
age = 25
print(f"姓名：{name}, 年龄：{age}")  # 输出：姓名：Alice, 年龄：25
num = 3.14159
print(f"宽度限制：{num:5}")  # 输出：宽度限制：3.14159
print(f"小数精度：{num:.2f}")  # 输出：小数精度：3.14
print(f"宽度和精度：{num:<7.2f}")  # 输出：宽度和精度：3.14
