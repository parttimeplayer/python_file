import random


salary_sum = 10000
for no in range(1, 20):
    score = random.randint(1, 10)
    if(salary_sum < 1000):
        break
    if(score < 5):
        continue
    else:
        salary_sum -= 1000
    print(f"第{no}名员工发工资1000元")