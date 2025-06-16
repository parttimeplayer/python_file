print(type(321))  
int_type = type(876)   # 把整型变量储存给int_type
print(int_type)


print(type(str(123)),"   ", str(123))        #将整型转化为字符串
print(int("123"))                            #将字符串转化为整型()
print(float("2.1"))                          #将字符串转化为浮点型

print(int(12.3))                             #会去掉小数点之后的部分，丢失精度
print(float(11))                             #会在整数后面加.0 