def main_menu(name,amount):
    print("------------------- 主菜单 -------------------")
    print(f"{name}，您好，欢迎来到黑马银行ATM，请选择操作：")
    print("查询余额\t【输入1】")
    print("存款\t\t【输入2】")
    print("取款\t\t【输入3】")
    print("退出\t\t【输入4】")
    choice = int(input())
    if choice == 1:
        query(True)
        return 1
    elif choice == 2:
        saving()
        return 1
    elif choice == 3:
        takeout()
        return 1
    elif choice == 4:
        print("程序退出")
        return None
    else:
        print("输入错误, 程序退出")
        return None
    


def query(query_args):
    if query_args:
        print("------------------- 查询余额 -------------------")
    print(f"当前您的余额为{money}")
 

def saving():
    print("------------------- 存款 -------------------")
    amount = int(input("请输入您要存款的数量："))
    global money
    money += amount
    query(False)


def takeout():
    print("------------------- 取款 -------------------")
    amount = int(input("请输入您要取款的数量："))
    global money
    money -= amount
    query(False)


money = 5000000
name = input("请输入您的姓名:")
while(1):
    if not main_menu(name, money):
        break
    