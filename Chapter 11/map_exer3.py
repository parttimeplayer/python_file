import json
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts



f = open("D:/python_learn/疫情.txt", "r", encoding="UTF-8")
data = f.read()
f.close()
data_dict = json.loads(data)
data_prov_list = data_dict["areaTree"][0]["children"]
map_data = []
for data_prov in data_prov_list:
    if data_prov["name"] == "河南省":
        data_henan = data_prov["children"]
for data_henan_children in data_henan:
    children_name = data_henan_children["name"] + "市"
    children_confirm = data_henan_children["total"]["confirm"]
    map_data.append((children_name, children_confirm))
map = Map()
map.add("河南疫情地图", map_data, "河南")
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 9, "label": "1-9人", "color": "#CCFFFF"},
            {"min": 10, "max": 49, "label": "10-49人", "color": "#FFFF00"},
            {"min": 50, "max": 99, "label": "50-99人", "color": "#FF9912"},
            {"min": 100, "max": 1000000000000000, "label": "100人以上", "color": "#FF3333"},
        ]
    )
)
map.render("河南疫情地图.html")

