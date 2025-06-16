# 封装数据
class Record:
    def __init__(self, date, id, amount, province):
        self.date = date
        self.id = id
        self.amount = amount
        self.province = province

    def __str__(self):
        return f"{self.date}, {self.id}, {self.amount}, {self.province}"