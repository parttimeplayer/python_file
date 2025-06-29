my_list = [["a", 33], ["b", 55], ["c", 11]]

# 排序，基于带名函数
def choose_sort_key(element):
    return element[1]

my_list.sort(key=choose_sort_key, reverse=True)

# 排序，基于lambda函数
my_list = [["a", 33], ["b", 55], ["c", 11]]
my_list.sort(key=lambda element: element[1], reverse=True)
print(my_list)