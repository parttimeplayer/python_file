f = open("D:/python_learn/test.txt", "w", encoding = "UTF-8")  #w模式会将文件之前的内容覆盖
f.write("Hello World")  #将内容写到内存里
# f.flush()    #将内存中积攒的内容，写到硬盘中
f.close()      #close()方法内置flush()方法