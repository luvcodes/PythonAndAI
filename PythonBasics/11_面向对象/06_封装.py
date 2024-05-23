"""
演示面向对象封装思想中私有成员的使用
"""


# 定义一个类，内含私有成员变量和私有成员方法
class Phone:
    # 使用双下划线开头的变量和方法，表示私有成员
    __current_voltage = 0.5

    def __keep_single_core(self):
        print("让CPU以单核模式运行")

    def call_by_5g(self):
        if self.__current_voltage >= 1:
            print("5g通话已开启")
        else:
            self.__keep_single_core()
            print("电量不足，无法使用5g通话，并已设置为单核运行进行省电。")


phone = Phone()
phone.call_by_5g()


# 示例二
class Employee:
    def __init__(self, name, salary):
        self.__name = name  # 私有属性
        self.__salary = salary  # 私有属性

    def get_name(self):
        """公有方法，获取员工姓名"""
        return self.__name

    def set_name(self, name):
        """公有方法，设置员工姓名"""
        self.__name = name

    def get_salary(self):
        """公有方法，获取员工薪水"""
        return self.__salary

    def set_salary(self, salary):
        """公有方法，设置员工薪水"""
        if salary > 0:
            self.__salary = salary
        else:
            print("薪水必须为正值")

    def display_info(self):
        """公有方法，显示员工信息"""
        print(f"Name: {self.__name}, Salary: {self.__salary}")

# 创建 Employee 对象
emp = Employee("John Doe", 50000)

# 通过公有方法访问私有属性
print(emp.get_name())  # 输出: John Doe
emp.set_salary(60000)
print(emp.get_salary())  # 输出: 60000

# 试图直接访问私有属性会导致错误
# print(emp.__name)  # AttributeError: 'Employee' object has no attribute '__name'

# 使用公有方法显示员工信息
emp.display_info()  # 输出: Name: John Doe, Salary: 60000

