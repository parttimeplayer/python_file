import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts


# 打开美国疫情数据的json文件
f_us = open("D:/python_learn/美国.txt","r", encoding = "UTF-8")
# 将文件中的数据读取
us_data = f_us.read()
# 处理掉文件开头不合json规范的内容
us_data = us_data.replace("jsonp_1629344292311_69436(", "")
# 处理掉文件结尾不合json规范的内容
us_data = us_data[ : -2]
# 将json数据转化为字典
us_dict = json.loads(us_data)
# 得到x轴数据
us_x_data = us_dict["data"][0]["trend"]["updateDate"][ : 314]
# 得到y轴数据
us_y_data = us_dict["data"][0]["trend"]["list"][0]["data"][ : 314]

# 同处理美国数据的方法一样，处理日本的数据
f_jp = open("D:/python_learn/日本.txt","r", encoding = "UTF-8")
jp_data = f_jp.read()
jp_data = jp_data.replace("jsonp_1629350871167_29498(", "")
jp_data = jp_data[ : -2]
jp_dict = json.loads(jp_data)
jp_x_data = jp_dict["data"][0]["trend"]["updateDate"][ : 314]
jp_y_data = jp_dict["data"][0]["trend"]["list"][0]["data"][ : 314]

# 同处理美国数据的方法一样，处理印度的数据
f_id = open("D:/python_learn/印度.txt","r", encoding = "UTF-8")
id_data = f_id.read()
id_data = id_data.replace("jsonp_1629350745930_63180(", "")
id_data = id_data[ : -2]
id_dict = json.loads(id_data)
id_x_data = id_dict["data"][0]["trend"]["updateDate"][ : 314]
id_y_data = id_dict["data"][0]["trend"]["list"][0]["data"][ : 314]

# 生成折线图对象
line = Line()
# 三个国家的日期一致，添加一个即可
line.add_xaxis(us_x_data)
# 添加三个国家的y轴数据，数据太多，通过label_opts功能隐藏
line.add_yaxis("美国确诊人数", us_y_data, label_opts = LabelOpts(is_show = False))
line.add_yaxis("日本确诊人数", jp_y_data, label_opts = LabelOpts(is_show = False))
line.add_yaxis("印度确诊人数", id_y_data, label_opts = LabelOpts(is_show = False))
line.set_global_opts(
    title_opts= TitleOpts(title= "全球新冠确诊人数", pos_left= "center", pos_bottom= "1%"),
)
line.render()

# 关闭文件
f_us.close()
f_id.close()
f_jp.close()