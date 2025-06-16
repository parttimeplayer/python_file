"""
文件处理相关的工具模块
"""



def print_file_info(file_name):
    """
    功能是将给定路径的文件内容输出到控制台中
    :param file_name:文件路径名称
    :return:None
    """
    f = None
    try:
        f = open(file_name, "r", encoding = "UTF-8")
        print(f.read())
    except:
        print("文件不存在")
    finally:
        if f: # 如果变量是None，表示False，如果有任何内容，就是True
            f.close()

def append_to_file(file_name, data):
    """
    将指定数据追加到指定文件中
    :param file_name:追加文件的路径
    :param data:要追加的数据
    :return:Nonw
    """
    f = open(file_name, "a", encoding = "UTF-8")
    f.write(data)
    f.close()



if __name__ == '__main__':
    print_file_info("D:/python_learn/word.txt")
    append_to_file("D:/python_learn/word.txt", "\nFinish")
    print_file_info("D:/python_learn/word.txt")