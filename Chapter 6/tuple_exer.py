"""
tuple里只有一个元素要在元素后面加逗号，否则就不是元组
元组中的元素不可以被修改
但是嵌套list里的内容可以修改
"""

num_tuple = (1, 2, 3, 4, 5, 3)

index = num_tuple.index(3) #index方法，寻找元素第一次出现的下标索引
print(f"元素3的下标索引是{index}")

times = num_tuple.count(3) #count方法，统计元组中元素出现的个数
print(f"元素3出现的次数为{times}")