from data import *
from filereader import *
from pyecharts.charts import Bar
from pyecharts.options import LabelOpts

textreader = TextReader("D:/python_learn/2011年1月销售数据.txt")
record1 = textreader.filereader()

jsonreader = JsonReader("D:/python_learn/2011年2月销售数据JSON.txt")
record2 = jsonreader.filereader()

allrecord = record1 + record2

allrecorddir = {}
for record in allrecord:
    try:
        allrecorddir[record.date] += record.amount
    except KeyError:
        allrecorddir[record.date] = record.amount 
bar = Bar()
bar.add_xaxis(list(allrecorddir.keys()))
bar.add_yaxis("销售额", list(allrecorddir.values()), label_opts=LabelOpts(is_show=False))
bar.render("2011年1-2销售额.html")

