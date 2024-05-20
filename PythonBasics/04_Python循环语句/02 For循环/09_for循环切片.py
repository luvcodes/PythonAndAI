# 指定首尾索引
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# 指定尾索引
print(players[:4])

# 指定首索引
print(players[2:])

# 指定负数索引
print(players[-3:])

# 循环中指定切片
for name in players[:3]:
    print(name.title())
