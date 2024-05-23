from pathlib import Path
import json

# # 定义文件路径
# path = Path('numbers.json')
#
# # 从文件读取内容并解析为Python对象
# try:
#     contents = path.read_text()
#     json_data = json.loads(contents)
#     print(json_data)
# except Exception as e:
#     print(f"读取或解析JSON文件时出错: {e}")

path = Path('username.json')

try:
    contents = path.read_text()
    username = json.loads(contents)
    print(f"Welcome back: {username}")
except Exception as e:
    print(f"读取或解析JSON文件时出错: {e}")
