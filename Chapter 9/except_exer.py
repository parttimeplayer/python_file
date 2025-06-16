# 基本捕获异常的语法
try:
    f = open("except.txt", "r", encoding = "UTF-8")
except:
    print("打开的文件不存在，创建新文件")
    f = open("except.txt", "w", encoding = "UTF-8")
finally:
    f.close() #无论无何都要执行的代码

# 捕获特定的异常
# try:
#     print(name)
# except NameError as e:
#     print("出现了未定义的变量")

# 捕获多个异常
try:
    1/0
except (NameError, ZeroDivisionError):
    print("出现了未定义变量的异常或者除零异常")

# 捕获所有异常
try:
    1/0
except Exception as e:
    print("出现异常了")
else:
    print("没有出现异常")  # 没有出现异常执行的代码

# 异常具有传递性，函数的连环调用也会捕获