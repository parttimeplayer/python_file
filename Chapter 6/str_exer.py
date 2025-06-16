"""
字符串是不可修改的数据容器
"""

my_str = "          itheima and icast "

index = my_str.index("and") #index方法查找元素第一次出现的起始位置
print(f"字符串and的起始位置是{index}")

new_str = my_str.replace("and", "or") #replace方法，将原字符串的参数1全部用参数2替代，得到一个新的字符串
print(new_str)

my_list = my_str.split(" ") #split方法，将字符串切割得到一个新的列表
print(f"切割后的列表为{my_list}，列表长度为{len(my_list)}")

new_str2 = my_str.strip() #strtp方法，规整操作，将字符串前后的元素规整，不传入参数，默认取出首尾空格换行符
print(new_str2)

my_str = "1212itheima and icast121"
new_str2 = my_str.strip("12")
print(new_str2)

times = my_str.count("12") #count方法，统计某个字符串出现的个数
print(f"字符串12出线的次数为{times}")