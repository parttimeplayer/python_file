import winsound



class Clock:
    id = None
    price = None
    def ring(self):
        winsound.Beep(2000, 3000) # (frequence, time)       


class Student:
    # 构造方法，会自动运行 
    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
    # 魔术方法，类对象变为字符串
    def __str__(self):
        return f"Student对象, 姓名为{self.name}, 年龄为{self.age}"
    # 魔术方法，类对象小于比较
    def __lt__(self, other):
        return self.age < other.age
    # 魔术方法，类对象小于等于比较
    def __le__(self, other):
        return self.age <= other.age
    # 魔术方法，类对象等于比较
    def __eq__(self, other):
        return self.age == other.age

# stu1 = Student("张三", 12, 123456)
# stu2 = Student("李四", 15, 124355)
# print(stu1 < stu2)
# print(stu1 > stu2)

class Phone:
    # 成员变量以__开头变为私有
    __current_voltage = None
    # 成员方法以__开头变为私有
    def __keep_single_core(self):
        print("CPU单核运行")


    