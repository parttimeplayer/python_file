#Practice2
i = 1
while (i <= 9):
    j = 1
    str1 = ""
    # end = ''控制不换行 \t控制距离
    while (j <= i):
        print(f"{j} * {i} = {j * i}\t", end = '')
        j += 1
    i += 1
    print()