"""
练习题
"""

# # 练习题一
# # 遍历列表，对于其中每种三明治，打印消息，并将其移动到另一个列表中，打印新列表内容
# sandwich_orders = ['leg ham', 'mayo', 'roast beef', 'meatball']
# finished_sandwiches = []
# index = 0
# # 按顺序 正序添加
# while index < len(sandwich_orders):
#     print(f"I made your tuna sandwich.")
#     finished_sandwiches.append(sandwich_orders[index])
#     index += 1
#
# # 倒序从后往前添加的
# # while index < len(sandwich_orders):
# #     print(f"I made your tuna sandwich.")
# #     finished_sandwiches.append(sandwich_orders.pop())
#
# print(finished_sandwiches)


# 练习题二
# 确保pastrami在列表中至少出现了三次
# 1. 打印一条消息指出pastrami卖完了
# 2. 使用while循环将列表中的pastrami都删除
# 3. 确认最后列表finished_sandwiches中不包含pastrami
sandwich_orders = ['leg ham', 'pastrami', 'mayo', 'pastrami', 'roast beef', 'pastrami', 'meatball']
finished_sandwiches = []
print("The pastrami are sold out!")
index = 0
while index < len(sandwich_orders):
    print(f"I made your tuna sandwich. ")
    finished_sandwiches.append(sandwich_orders[index])
    if sandwich_orders[index] == 'pastrami':
        sandwich_orders.remove(sandwich_orders[index])
    index += 1

for sandwich in finished_sandwiches:
    print(sandwich)

# 练习题三
responses = {}
polling_active = True
while polling_active:
    name = input("What is your name? ")
    response = input("If you could visit one place in the world, where would you go? ")
    # 存储到字典中
    responses[name] = response
print("\n--- Polling result ---")
for name, response in responses.items():
    print(f"Name: {name}, response: {response}")
