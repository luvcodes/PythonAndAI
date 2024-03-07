# set1 = {1, 2, 3}
# set2 = {1, 5, 6}
# set3 = set1.difference(set2)
# print(f"取出差集后的结果是：{set3}")
# print(f"取差集后，原有set1的内容：{set1}")
# print(f"取差集后，原有set2的内容：{set2}")

# 消除2个集合的差集
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set1.difference_update(set2)
print(f"消除差集后，集合1结果：{set1}")
print(f"消除差集后，集合2结果：{set2}")
