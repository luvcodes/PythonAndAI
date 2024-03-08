"""
演示面向对象：继承中
对父类成员的复写和调用
"""


class Phone:
    IMEI = None
    producer = "ITCAST"

    def call_by_5g(self):
        print("使用5g网络进行通话")


# 定义子类，复写父类成员
class MyPhone(Phone):
    # 复写父类的成员属性
    producer = "ITHEIMA"

    def call_by_5g(self):
        print("开启CPU单核模式，确保通话的时候省电")

        # 在子类中，调用父类成员
        # 方式1 通过父类名来调用
        # print(f"父类的厂商是：{Phone.producer}")
        # Phone.call_by_5g(self)

        # 方式2 通过super()方法来调用
        print(f"父类的厂商是：{super().producer}")
        super().call_by_5g()

        print("关闭CPU单核模式，确保性能")


phone = MyPhone()
phone.call_by_5g()
# 查看子类的成员属性值
print(phone.producer)
