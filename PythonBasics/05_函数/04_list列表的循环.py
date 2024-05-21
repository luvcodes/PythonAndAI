"""
演示对list列表的循环，使用while和for循环2种方式
"""


def list_while_func():
    """
    使用while循环遍历列表的演示函数
    :return: None
    """
    my_list = ["传智教育", "黑马程序员", "Python"]
    index = 0
    while index < len(my_list):
        element = my_list[index]
        print(f"列表的元素：{element}")
        index += 1


def list_for_func():
    """
    使用for循环遍历列表的演示函数
    :return: None
    """
    my_list = [1, 2, 3, 4, 5]
    for element in my_list:
        print(f"列表的元素有：{element}")


list_while_func()
list_for_func()
