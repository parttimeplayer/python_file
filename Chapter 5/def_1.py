def my_len(str1):
    """
    my_len函数可以接收一个字符串，返回其长度。
    param str1: 形参str1表示一个字符串
    return:返回值是形参str1的长度
    """
    len1 = 0
    for x in str1:
        len1 += 1
    return len1
    
str1 = "fdfadgd"
print(my_len(str1))

# global 全局变量