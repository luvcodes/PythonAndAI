"""
演示：定义函数返回值的语法格式
"""


# # 定义一个函数，完成2数相加功能
# def add(a, b):
#     result = a + b
#     # 通过返回值，将相加的结果返回给调用者
#     return result
#     # 返回结果后，还想输出一句话
#     print("我完事了")
#
#
# # 函数的返回值，可以通过变量去接收
# r = add(5, 6)
# print(r)


# 类型一: 返回简单的值
def get_formatted_name(first_name, last_name):
    """返回标准格式的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)


# 类型二: 可选实参
def get_formatted_name2(first_name, last_name, middle_name=''):
    """返回标准格式的姓名"""
    if middle_name: # 检查 middle_name 是否有值
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


withoutMiddleName = get_formatted_name2('jimi', 'hendrix')
print(withoutMiddleName)
withMiddleName = get_formatted_name2('john', 'hooker', 'lee')
print(withMiddleName)

# 类型三: 返回字典
def build_person(first_name, last_name):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    return person

print(build_person('jimi', 'hendrix'))

# 类型三：返回字典 扩展参数
def build_person2(first_name, last_name, age=None):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

print(build_person2('jimi', 'hendrix', 27))

