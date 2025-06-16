name = "\"Hello World"   # 用\消除“的作用


# 打印中的字符串拼接

print("Hello" + "World") # 将字符串直接拼接在一起
print("Hello" , "World") # 字符串之间有空格

tel = 4223641
address = "新建路69号"

print("我的办公电话是" + str(tel) + "，办公地址是" + address)  # 必须将整型转为字符串才可以拼接

"""
    字符串格式化(format)
    方法1：
    %s  内容转化为字符串放入占位的位置
    %f  内容转化为浮点型放入占位的位置    用m.n控制宽度和小数位数
    %d  内容转化为整型放入占位的位置
    方法2：
    字符串前加f，中间用{变量名/表达式}占位
"""

message = "我的办公电话是%s, 办公地址是%s" % (tel, address) # %表示占位，s表示把变量换成字符串放入占位的位置
print(message)  

avg_salary = 5647.7534
message = "太原市的平均工资是%.2f" % avg_salary
print(message)  
message = "太原市的平均工资是%8.2f" % avg_salary
print(message)  
message = f"我的办公电话是{tel}, 办公地址是{address}"
print(message)  


# Practice
name = "传智播客"
stock_code = "003032"
stock_price = 19.99
stock_price_daily_growth_factor = 1.2
growth_days = 7
print(f"公司：{name}，股票代码：{stock_code}，当前股价：{stock_price}")
print("每日增长系数是：%.2f，经过%d天的增长后，股价达到了%.2f" % (stock_price_daily_growth_factor,
                                             growth_days, stock_price*stock_price_daily_growth_factor**7))
