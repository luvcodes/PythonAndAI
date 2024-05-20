# 数到20
# for value in range(1, 21):
#     print(value)
# print('----')

# 100万
# million = [value for value in range(1, 1000_001)]
# print(million)

# 100万求和
million = []
for value in range(1, 1000_001):
    million.append(value)
print('Min: ' + str(min(million)) + ', Max: ' + str(max(million)) + '. Sum: ' + str(sum(million)))

# 奇数
odd_number = []
for value in range(1, 21, 2):
    odd_number.append(value)
print(odd_number)

# 3的倍数
timesThree = []
for value in range(3, 31):
    if value % 3 == 0:
        timesThree.append(value)
print(timesThree)

# 立方
cube = []
for value in range(1, 11):
    cube.append(value ** 3)
print(cube)

# 立方推导式
firstTenCube = [value ** 3 for value in range(1, 11)]
print(firstTenCube)

