from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts



# 构建对象
map = Map()
# 寻找数据
data = [
    ("北京市", 99),
    ("上海市", 199),
    ("湖南省", 299),
    ("台湾省", 399),
    ("广东省", 499)
]
# 添加数据
map.add("测试地图", data, "china")
# 设置全局选项
map.set_global_opts(
    visualmap_opts = VisualMapOpts(
        # 添加颜色
        is_show = True, 
        # 手动校准颜色对应的范围
        is_piecewise = True, 
        # color的颜色代码在RGB颜色对照表中寻找
        pieces = [
            {"min": 1, "max": 99, "label": "1-99", "color": "#CCFFFF"}, 
            {"min": 100, "max": 299, "label": "100-299", "color": "#FF6666"}, 
            {"min": 300, "max": 500, "label": "300-500", "color": "#990033"} 
        ]
    )
)
# 绘图
map.render()