# 获取全部的key
my_dict = {"周杰轮": 99, "林俊节": 88, "张学油": 77}
keys = my_dict.keys()
print(f"字典的全部keys是：{keys}")
print("---------")

# 遍历字典
# 方式1：通过获取到全部的key来完成遍历
for key in keys:
    print(f"字典的key是:{key}")
    print(f"字典的value是：{my_dict[key]}")
print('----------')

# 方式2：直接对字典进行for循环，每一次循环都是直接得到key
for key in my_dict:
    print(f"2字典的key是:{key}")
    print(f"2字典的value是：{my_dict[key]}")
print("----------")

# 方式3: for循环使用items方法
for key, value in my_dict.items():
    print(f"3字典的key: {key}")
    print(f"3字典的value: {value}")

# 按照特定顺序sorted遍历字典
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for learning {favorite_languages[name]}")
print("--------------------")

# 获取字典中的所有值
for language in favorite_languages.values():
    print(language.title())



