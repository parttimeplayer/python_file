"""
r:只读
w:写入
a:追加
"""

f = open("D:/python_learn/file_oper_r.txt", "r", encoding = "UTF-8")
print(f.read(10)) #read(num) 方法，读取num个字节的文字,以字符串输出
print(f.read())   #多次调用read，会从上一次调用的结尾处继续读取

lines = f.readlines()  #readlines()方法，读取全部内容，封装到列表中

line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)

for line in f:         #用循环读取文件
    print(line)

f.close()   #停止占用文件


# 另一种文件打开方式，可以自动关闭文件  
with open("D:/python_learn/file_oper_r.txt", "r", encoding = "UTF-8") as f:
    for line in f:     
        print(line)


# exer 方法1
with open("D:/python_learn/word.txt", "r", encoding = "UTF-8") as f:
    text = f.read()
    print(text.count("itheima"))

#方法2
count = 0
with open("D:/python_learn/word.txt", "r", encoding = "UTF-8") as f:
    for line in f:
        line = line.strip()
        words = line.split(" ")
        for word in words:
            if word == "itheima":
                count += 1
print(count)
    
