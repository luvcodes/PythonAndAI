"""
演示字典的常用操作
"""
my_dict = {"周杰轮": 99, "林俊节": 88, "张学油": 77}

# 新增元素
my_dict["张信哲"] = 66
print(f"字典经过新增元素后，结果：{my_dict}")

# 更新元素
my_dict["周杰轮"] = 33
print(f"字典经过更新后，结果：{my_dict}")

# 删除元素 pop
score = my_dict.pop("周杰轮")
print(f"字典中被移除了一个元素，结果：{my_dict}, 周杰轮的考试分数是：{score}")

# 删除元素 del 永久删除
del my_dict["张学油"]
print(f"字典中被移除了一个元素，结果是: {my_dict}, 张学油的考试分数是: {my_dict['张学油']}")

# 清空元素, clear
my_dict.clear()
print(f"字典被清空了，内容是：{my_dict}")

# get方法获取键对应的值, 键不存在 返回指定默认值
alient_0 = {'color': 'green', 'speed': 'slow'}
point_value = alient_0.get('personality', 'No personality info included')
print(point_value)

# 统计字典内的元素数量, len()函数
num = len(my_dict)
print(f"字典中的元素数量有：{num}个")
