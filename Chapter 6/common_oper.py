my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_str = "abcdefg"
my_set = {1, 2, 3, 4, 5}
my_dict = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}

#max方法，寻找容器中的最大值
my_list_max = max(my_list)
print(f"列表中的最大值是{my_list_max}")
my_tuple_max = max(my_tuple)
print(f"元组中的最大值是{my_tuple_max}")
my_str_max = max(my_str)
print(f"字符中的最大值是{my_str_max}")
my_set_max = max(my_set)
print(f"集合中的最大值是{my_set_max}")
my_dict_max = max(my_dict)
print(f"字典中的最大值是{my_dict_max}")

#min方法，寻找容器中的最小值my_list_max = max(my_list)
my_list_min = min(my_list)
print(f"列表中的最大值是{my_list_min}")
my_tuple_min = min(my_tuple)
print(f"元组中的最大值是{my_tuple_min}")
my_str_min = min(my_str)
print(f"字符中的最大值是{my_str_min}")
my_set_min = min(my_set)
print(f"集合中的最大值是{my_set_min}")
my_dict_min = min(my_dict)
print(f"字典中的最大值是{my_dict_min}")

#list()方法，容器转列表
print(f"列表转列表的结果是{list(my_list)}")
print(f"元组转列表的结果是{list(my_tuple)}")
print(f"字符转列表的结果是{list(my_str)}")
print(f"集合转列表的结果是{list(my_set)}")
print(f"字典转列表的结果是{list(my_dict)}")

#tuple()方法，容器转元组
print(f"列表转元组的结果是{tuple(my_list)}")
print(f"元组转元组的结果是{tuple(my_tuple)}")
print(f"字符转元组的结果是{tuple(my_str)}")
print(f"集合转元组的结果是{tuple(my_set)}")
print(f"字典转元组的结果是{tuple(my_dict)}")

#str()方法，容器转字符串
print(f"列表转字符串的结果是{str(my_list)}")
print(f"元组转字符串的结果是{str(my_tuple)}")
print(f"字符转字符串的结果是{str(my_str)}")
print(f"集合转字符串的结果是{str(my_set)}")
print(f"字典转字符串的结果是{str(my_dict)}")

#set()方法，容器转集合
print(f"列表转集合的结果是{set(my_list)}")
print(f"元组转集合的结果是{set(my_tuple)}")
print(f"字符转集合的结果是{set(my_str)}")
print(f"集合转集合的结果是{set(my_set)}")
print(f"字典转集合的结果是{set(my_dict)}")

#sorted方法，对容器进行排序
my_list = [4, 1, 2, 5, 3]
my_tuple = (4, 1, 2, 5, 3)
my_str = "gshavb"
my_set = {4, 1, 2, 5, 3}
my_dict = {"key4": 1, "key1": 2, "key2": 3, "key5": 4, "key3": 5}
print(f"列表排序的结果是{sorted(my_list)}")
print(f"元组排序的结果是{sorted(my_tuple)}")
print(f"字符排序的结果是{sorted(my_str)}")
print(f"集合排序的结果是{sorted(my_set)}")
print(f"字典排序的结果是{sorted(my_dict)}")

print(f"列表反向排序的结果是{sorted(my_list, reverse = True)}")
print(f"元组反向排序的结果是{sorted(my_tuple, reverse = True)}")
print(f"字符反向排序的结果是{sorted(my_str, reverse = True)}")
print(f"集合反向排序的结果是{sorted(my_set, reverse = True)}")
print(f"字典反向排序的结果是{sorted(my_dict, reverse = True)}")