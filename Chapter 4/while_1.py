import random


i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print(f"1-100的和是{sum}")

#Practice
time = 0
target = random.randint(1,100)
condition = True  # Flag
while(condition):
    guess_num = int(input("请输入您猜想的数字："))
    time += 1
    if guess_num == target:
        condition = False
    elif guess_num > target:
        print("猜大了")
    else:
        print("猜小了")
print(f"您猜对了，猜了{time}次")

