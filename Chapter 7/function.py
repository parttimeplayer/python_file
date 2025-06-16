"""
返回值可以返回多个。
例如：return 1，2
主函数中用 x,y = 来接收
"""

"""
传参时可以用位置传参，也可以用关键字传参，二者也可以混用，但是位置传参必须在前
缺省参数，在函数中直接设置默认值
"""

#不定长 - 位置不定长

def no_len_loc(*args): #可以传入多个参数，会以元组的形式存在
    return print(args)

no_len_loc("Hello", "World", "Jy")

#不定长 - 关键字不定长

def no_len_key(**kwargs):   #可以传入多个参数，会以字典的形式存在
    return print(kwargs)


no_len_key( name = "Hello", age = 10, gender = "Male")

# 函数作为参数传递
def test_func(add):
    print(add(1, 2), type(add))

def add(x, y):
    return x + y

def minus(x, y):
    return x - y

test_func(minus)

# 匿名函数
test_func(lambda x, y: x * y) # 函数执行体只能写一行