from pyecharts.charts import Bar
from pyecharts.options import LabelOpts



bar = Bar()
bar.add_xaxis(["中国", "美国", "英国"])
# LabelOpts设置数字的位置
bar.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position="right"))
# 反转x轴y轴
bar.reversal_axis()
bar.render("基础柱状图.html")