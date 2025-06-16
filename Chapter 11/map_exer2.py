import json
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts,TitleOpts



f = open("D:/python_learn/疫情.txt", "r", encoding="UTF-8")
data = f.read()
data_dict = json.loads(data)
f.close()
map = Map()
map_data = []
children_list = data_dict["areaTree"][0]["children"]
length = len(children_list)
for i in range(length):
    map_data.append((children_list[i]["name"], children_list[i]["total"]["confirm"]))
map.add("全国疫情确诊地图", map_data, "china")
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图", pos_left="center",pos_bottom="1%"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 9, "label": "1-9人", "color": "#CCFFFF"},
            {"min": 10, "max": 99, "label": "10-99人", "color": "#FFFF00"},
            {"min": 100, "max": 499, "label": "100-499人", "color": "#FF9912"},
            {"min": 500, "max": 999, "label": "500-999人", "color": "#FF8000"},
            {"min": 1000, "max": 9999, "label": "1000-9999人", "color": "#FF6666"},
            {"min": 10000, "max": 10000000000, "label": "10000人以上", "color": "#990033"}
        ]
    )
)
map.render("全国疫情地图.html")
