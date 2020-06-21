# json是轻量级数据交换格式，python语言通过json模块中的方法实现json格式与python格式转换
import json


python_data = {'name': 'ACME', 'age': '18', 'grade': '90'}
# dumps方法，将python数据转换为json数据，参数sort_keys、indent等可选
json_data = json.dumps(python_data, sort_keys=True, indent=1)


# dump方法，将python数据转换为json数据，写入文件
with open('json.txt', 'w') as f:
    json.dump(python_data, f)


# loads方法：将json数据转换为python数据，注意json数据字符串为双引号
python_data_ = json.loads(json_data)


# load方法：读取json文件，将其转化为python数据
with open('json.txt', 'r') as f:
    python_data__ = json.load(f)
