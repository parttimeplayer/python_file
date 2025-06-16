import my_utils.str_util  #下面调用必须要写全
from my_utils import file_util #下面调用可以直接用file_util模块

__all__ = ["test_a"] # 表示外部调用时，*所能使用的函数 ，在包中，要放在__init__文件中

"""
导入不同模块的同名功能，后一个功能会把前一个覆盖     
"""

# __main__变量,如果内部调用，name就是main，外部调用就不是
if __name__ == '__main__':
    print("Hello World")

"""
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 包名称   下载速度更快
"""