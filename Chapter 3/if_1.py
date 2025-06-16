import random

print("欢迎来到黑马儿童游乐场，儿童免费，成人收费。")
age = int(input("请输入您的年龄："))

if age >= 60:
    print("您是老年人，可以免费游玩。")
elif age >= 18:
    print("您已成年，游玩需要补票10元。")
else:
    print("您未成年，可以免费游玩")
print("祝您游玩愉快。")


#Practice
asw = 10
if int(input("请输入第一次猜想的数字：")) == asw:
    print("恭喜你猜对啦")
elif int(input("不对，再猜一次：")) == asw:
    print("恭喜你猜对啦")
elif int(input("不对，再猜最后一次：")) == asw:
    print("恭喜你猜对啦")
else:
    print(f"Sorry，全部猜错啦，我想的是{asw}")

#Practice 2
num = random.randint(1 , 10)
guess_num = int(input("请输入您猜想的数字："))
if guess_num > num:
    print("猜大了")
    guess_num = int(input("请输入您第二次猜想的数字："))
    if guess_num > num:
        print("猜大了")
        guess_num = int(input("请输入您第三次猜想的数字："))
        if guess_num > num:
            print("猜大了，游戏结束")
        elif guess_num < num:
            print("猜小了，游戏结束")
        else:
            print("猜对了")
    elif guess_num < num:
        print("猜小了")
        guess_num = int(input("请输入您第三次猜想的数字："))
        if guess_num > num:
            print("猜大了，游戏结束")
        elif guess_num < num:
            print("猜小了，游戏结束")
        else:
            print("猜对了")
    else:
        print("猜对了")
elif guess_num < num:
    print("猜小了")
    guess_num = int(input("请输入您第二次猜想的数字："))
    if guess_num > num:
        print("猜大了")
        guess_num = int(input("请输入您第三次猜想的数字："))
        if guess_num > num:
            print("猜大了，游戏结束")
        elif guess_num < num:
            print("猜小了，游戏结束")
        else:
            print("猜对了")
    elif guess_num < num:
        print("猜小了")
        guess_num = int(input("请输入您第三次猜想的数字："))
        if guess_num > num:
            print("猜大了，游戏结束")
        elif guess_num < num:
            print("猜小了，游戏结束")
        else:
            print("猜对了")
    else:
        print("猜对了")
else:
    print("猜对了")
