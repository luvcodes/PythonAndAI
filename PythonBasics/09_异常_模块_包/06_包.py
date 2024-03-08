"""
演示Python的包
"""

# 创建一个包
# 导入自定义的包中的模块，并使用
# 方式一 用import语句
# import PythonBasics.my_package.my_module1
# import PythonBasics.my_package.my_module2
# PythonBasics.my_package.my_module1.info_print1()
# PythonBasics.my_package.my_module2.info_print2()

# 方式二 用from语句
# from PythonBasics.my_package import my_module1
# from PythonBasics.my_package import my_module2
# my_module1.info_print1()
# my_module2.info_print2()

# 方式三 用from语句import到具体的方法名
# from PythonBasics.my_package.my_module1 import info_print1
# from PythonBasics.my_package.my_module2 import info_print2
# info_print1()
# info_print2()

# 通过__all__变量，控制import *
from PythonBasics.my_package import *
my_module1.info_print1()
# my_module2.info_print2()
