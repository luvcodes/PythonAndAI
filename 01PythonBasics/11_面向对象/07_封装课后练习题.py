"""
讲解面向对象-封装特性课后练习题
设计带有私有成员的手机
"""


class Phone:
    # 提供私有成员变量
    __is_5g_enable = True

    # 提供私有成员方法
    def __check_5g(self):
        if self.__is_5g_enable:
            print("5g开启")
        else:
            print("5g关闭，使用4g网络")

    # 提供公开成员方法
    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")


phone = Phone()
phone.call_by_5g()
