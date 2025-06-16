stu_score = {"王力宏": {"语文": 77, "数学": 66, "英语": 33}, 
             "周杰伦": {"语文": 88, "数学": 86, "英语": 55}, 
             "林俊杰": {"语文": 99, "数学": 96, "英语": 66}}
print(stu_score["王力宏"]["语文"])

stu1 = stu_score.pop("王力宏")   #pop方法，得到字典中key对应的value，并将其删除
print(f"王力宏的成绩是{stu1}")  

keys_list = stu_score.keys()    #keys方法，得到字典中所有的keys
print(f"学生姓名是{keys_list}")

for key in keys_list:
    print(stu_score[key])

stu_score.clear()  #clear方法，清空字典


#exer
stuff_info = {"王力鸿": {"部门": "科技部", "工资": 3000, "级别": 1},
            "周杰轮": {"部门": "市场部", "工资": 5000, "级别": 2},
            "林俊节": {"部门": "市场部", "工资": 7000, "级别": 3},
            "张学油": {"部门": "科技部", "工资": 4000, "级别": 1},
            "刘德滑": {"部门": "市场部", "工资": 6000, "级别": 2}}

for name in stuff_info:
    if stuff_info[name]["级别"] == 1:
        stuff_info[name]["级别"] += 1
        stuff_info[name]["工资"] += 1000
print("调整后的员工信息如下：")
print(stuff_info)
        