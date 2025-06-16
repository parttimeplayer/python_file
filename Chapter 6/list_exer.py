num_list = [0, 1, 2, 3, 4, 5]

args = num_list.index(3) #index方法查找元素的下标,如元素不存在报valueErr
print(args)

num_list.insert(0, -1) #insert方法在指定位置插入元素，第一个参数是索引，第二个是元素
print(num_list)

num_list.append(6) #append方法将元素追加到列表尾部
print(num_list)

num_list.extend([7, 8, 9]) #extend方法追加一批元素在列表尾部
print(num_list)

del num_list[0]  #del 删除某个元素
print(num_list)

num_pop = num_list.pop(9) #pop方法将某个元素取出，并在列表中删除
print(f"取出的元素是{num_pop}")
print(num_list)

num_list.remove(0) #remove方法 删除在列表中的第一个匹配项
print(num_list)

num_list.clear() #clear方法，清空列表
print(num_list)

num_list = [0, 0, 0, 1]
a = num_list.count(0) #count方法，统计某个元素的数量 
print(f"元素0的数量是{a}")

length = len(num_list)
print(f"列表的长度为{length}")
