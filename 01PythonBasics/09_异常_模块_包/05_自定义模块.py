"""
演示自定义模块
"""

# 导入自定义模块使用
# import my_module1
# my_module1.test(1, 2)
# from my_module1 import test
# test(1, 2)

# 导入不同模块的同名功能
# 这里证明的意思就是两个同名的方法，用的就是第二个test方法
# from my_module1 import test
# from my_module2 import test
# test(1, 2)

# __main__变量
# from my_module1 import test

# __all__变量
# 这里有两个条件才可以使用某一个方法
# 1. 使用了import *
# 2. all变量的数组中的定义
# 但是这里如果要手动调用test_b方法是不受这个all变量限制的
from my_module1 import *
test_a(1, 2)
# 在my_mmodule1中定义了__all__变量，这里就不能使用test_b了
# test_b(2, 1)
