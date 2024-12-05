"""
演示数据容器字典的定义
"""

# 定义字典
my_dict1 = {"王力鸿": 99, "周杰轮": 88, "林俊节": 77}

# 定义空字典
my_dict2 = {}
my_dict3 = dict()
print(f"字典1的内容是：{my_dict1}, 类型：{type(my_dict1)}")
print(f"字典2的内容是：{my_dict2}, 类型：{type(my_dict2)}")
print(f"字典3的内容是：{my_dict3}, 类型：{type(my_dict3)}")

# 定义重复Key的字典
my_dict1 = {"王力鸿": 99, "王力鸿": 88, "林俊节": 77}
print(f"重复key的字典的内容是：{my_dict1}")

# 从字典中基于Key获取Value
my_dict1 = {"王力鸿": 99, "周杰轮": 88, "林俊节": 77}
score = my_dict1["王力鸿"]
print(f"王力鸿的考试分数是：{score}")



# 从嵌套字典中获取数据
score = stu_score_dict["周杰轮"]["语文"]
print(f"周杰轮的语文分数是：{score}")
