f1 = open("D:/python_learn/bill.txt", "r", encoding = "UTF-8")
f2 = open("D:/python_learn/bill.txt.bak", "w", encoding = "UTF-8")

for line in f1:
    words = line.split("，")
    if words[4] == "测试\n":
        continue
    else:
        f2.write(line)
f1.close()
f2.close()