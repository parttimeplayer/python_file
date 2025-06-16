from pyecharts.charts import Bar, Timeline
from pyecharts.options import LabelOpts
from pyecharts.globals import ThemeType



f = open("D:/python_learn/1960-2019全球GDP数据.csv", "r", encoding="GB2312")
data_list = f.readlines()
f.close()
data_list.pop(0)
data_dict = {}
for data in data_list:
    year = int(data.split(",")[0])       # 年份
    country = data.split(",")[1]         # 国家
    gdp = float(data.split(",")[2])      # GDP,通过float把科学计数法转化为数字
    try:
        data_dict[year].append([country, gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country, gdp])
for key in data_dict:
    data_dict[key].sort(key = lambda element: element[1], reverse=True)
bar_list = []
for year in range(1960, 2020):
    country_List = []
    gdp_list = []
    for i in range (8):
        country_List.append(data_dict[year][i][0])
        gdp_list.append(data_dict[year][i][1])
    bar = Bar()
    bar.add_xaxis(country_List[::-1])
    bar.add_yaxis("GDP", gdp_list[::-1], label_opts=LabelOpts(
            position="right"))
    bar.reversal_axis()
    bar_list.append(bar)

timeline = Timeline({"theme":ThemeType.LIGHT})
year = 1960
for bar_data in bar_list:
    timeline.add(bar_data, year)
    year += 1
timeline.add_schema(
    is_auto_play=True,
    is_loop_play=True,
    play_interval=1000
)
timeline.render("1960-2019全球GDP数据排名前8的国家.html")