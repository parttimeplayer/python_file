import json



data = [{"name": "张大山", "age": 11}, {"name": "王大锤", "age": 11},{"name": "李小虎", "age": 11}]
json_str = json.dumps(data, ensure_ascii = False)   # 将列表转换为json格式，如果想中文展示，ensure_ascii 设置为FALSE
print(f"json_str的数据类型是{type(json_str)}，内容是{json_str}")

python_list = json.loads(json_str)  # 将json格式转换为列表
print(f"json_str的数据类型是{type(python_list)}，内容是{python_list}")

