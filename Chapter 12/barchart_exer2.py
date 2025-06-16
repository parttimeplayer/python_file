from pyecharts.charts import Bar, Timeline
from pyecharts.options import LabelOpts
from pyecharts.globals import ThemeType



bar1 = Bar()
bar1.add_xaxis(["中国", "美国", "英国"])
# LabelOpts设置数字的位置
bar1.add_yaxis("GDP", [30, 30, 20], label_opts=LabelOpts(position="right"))
# 反转x轴y轴
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(["中国", "美国", "英国"])
# LabelOpts设置数字的位置
bar2.add_yaxis("GDP", [50, 50, 50], label_opts=LabelOpts(position="right"))
# 反转x轴y轴
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(["中国", "美国", "英国"])
# LabelOpts设置数字的位置
bar3.add_yaxis("GDP", [70, 60, 60], label_opts=LabelOpts(position="right"))
# 反转x轴y轴
bar3.reversal_axis()

# 主题设置
timeline = Timeline({"theme": ThemeType.LIGHT})
timeline.add(bar1, "point 1")
timeline.add(bar2, "point 2")
timeline.add(bar3, "point 3")

# 自动播放设置
timeline.add_schema(
    play_interval=1000,    # 播放间隔时间，单位毫秒
    is_timeline_show=True,  # 是否显示时间线
    is_auto_play=True,     # 是否自动播放
    is_loop_play=True      # 是否循环播放
)
timeline.render("时间柱状图.html")