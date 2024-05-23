"""
json文件存储数据
"""

from pathlib import Path
import json
#
# numbers = [2, 3, 5, 7, 11, 13]
#
# path = Path('numbers.json')
# contents = json.dumps(numbers)
# path.write_text(contents)


# 保存和读取用户生成的数据
username = input("What is your name? ")
path = Path('username.json')
contents = json.dumps(username)
path.write_text(contents)
print(f"We'll remember when you come back, {username}")
