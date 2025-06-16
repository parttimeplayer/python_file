"""
字符串相关的工具模块
"""



def str_reverse(s):
    """
    功能是将字符串完成反转
    :param s:将被反转的字符串
    :return:反转得到的字符串
    """
    return s[ : :-1]

def substr(s, x, y):
    """
    功能是按照起始下标和结束下标截取字符串
    :param s:将被截取的字符串
    :param x:起始位置的下标
    :param y:结束位置的下标
    :return:得到的新的截取的字符串
    """
    return s[x : y] 


if __name__ == "__main__":
    print(str_reverse("黑马程序员"))
    print(substr("黑马程序员", 1, 3))
