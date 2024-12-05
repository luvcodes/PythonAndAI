# 列表嵌套字典
aliens = []
# 创建30个外星人
for alien in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# 显示前5个外星人
for i in aliens[:5]:
    print(i)

# for alien in range(5):
#     print(aliens[alien])
print("...")

print(f"Total number of aliens: {len(aliens)}")

# 字典嵌套列表
# 示例一
# 存储顾客所点比萨的信息
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# 概述顾客点的比萨
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")
print("-------------------------------------------")

# 示例二
favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"\n{name.title()}'s favorite language are: ")
        for language in languages:
            print(f"\t{language.title()}")
    else:
        print(f"\n{name.title()}'s favorte language is {languages}")

# 字典嵌套
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username.title()}")
    fullname = f"{user_info['first'].title()} {user_info['last'].title()}"
    location = f"{user_info['location'].title()}"

    print(f"\nFull name: {fullname}")
    print(f"Location: {location}")


