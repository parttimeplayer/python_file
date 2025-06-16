"""
不允许重复元素出现，无序，所以不支持下标索引访问,不能用while遍历
"""

set1 = {"你好", "Hello", "china", "america"}
set1.add("World") #add方法，向集合里添加元素
print(set1)
set1.remove("你好") #remove方法，从集合里取出元素
print(set1)
test = set1.pop() #pop方法，从集合里随机取一个元素并删除
print(f"随机取出的元素是{test}，剩余的集合是{set1}")
set1.clear()
print(set1)

set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.difference(set2) #difference方法，取出集合1有的而集合2没有的，得到一个新的集合，原本的集合不发生改变
print(f"集合1有的而集合2没有的{set3}")

set1.difference_update(set2) #difference_update方法，删除集合1里包含的集合2中的元素，集合1被修改
print(f"删除集合1里包含的集合2中的元素{set1}") 

set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.union(set2) #union方法，将两个集合合并
print(f"两个集合合并后的集合为{set3}")

length = len(set3) #len方法，统计集合中元素个数
print(f"集合3的元素个数为{length}")


#exer
my_list = ['黑马程序员', '传智播客', '黑马程序员', '传智播客', 'itheima', 'itcast', 'itheima', 'itcast', 'best']
my_set = set()
for i in my_list:
    my_set.add(i)
print(my_set)