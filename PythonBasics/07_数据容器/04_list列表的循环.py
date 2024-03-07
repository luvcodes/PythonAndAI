"""
演示使用while和for循环遍历列表
"""

def list_while_func():
    """
    使用while循环遍历列表的演示函数
    :return: None
    """
    mylist = ["传智教育", "黑马程序员", "Python"]
    index = 0
    while index < len(mylist):
        print(mylist[index])
        index += 1

def list_for_func():
    """
    使用for循环遍历列表的演示函数
    :return:
    """
    mylist = ["传智教育", "黑马程序员", "Python"]
    for item in mylist:
        print(item)


list_while_func()

list_for_func()
