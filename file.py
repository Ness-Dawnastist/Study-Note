pi_digits_file_path = 'D:/Programs/Python/pi_digits.txt'
"""使用一个变量来存储绝对路径"""
with open(pi_digits_file_path) as file_object:
    """如果要使用相对路径，需要在终端中调整工作区"""
    contents = file_object.read()
    print(contents.rstrip())

# 首先，函数open()打开文件，并返回一个表示文件的对象，这个对象存储在as后面的变量中
# with的作用是自动在合适的时间关闭文件，否则需要手动调用close()，容易出错
# read()读取文件的全部内容并存储在一个字符串中，
# 当到达文件末尾时，read()会额外返回一个空字符串，导致输出结果多出一行空行
# 可以使用方法.rstrip()来解决

# 可使用for循环每次读取一行
with open(pi_digits_file_path) as file_object:
    for line in file_object:
        print(line.rstrip())
        """Python中的文件对象在迭代时默认会按行返回文件内容"""
        """文件的每一行都以换行符结束，而print()自带换行符，所以要使用方法.rstrip()来去除换行符"""
        """如果不使用方法.rstrip()，则每一行之间都多了一行空行"""

# open返回的文件对象只在with代码块中可用
# 可以用方法.readlines()来将文件内容存储在列表中
with open(pi_digits_file_path) as file_object:
    lines = file_object.readlines() # lines就是一个存储着字符串的列表
    for line in lines:
        print(line.rstrip())

# 使用文件中的内容
with open(pi_digits_file_path) as file_object:
    lines = file_object.readlines()
    pi_string = ''
    for line in lines:
        pi_string += line.strip() # 每一行左右都有空格，所以用.strip()
    
    print(pi_string) # 这里打印的是字符串
    print(len(pi_string))
    print(float(pi_string)) # 转换为浮点数

# 写入文件
# 用到方法.open()的第二个参数
# .open('file_name', 'mode')
# mode参数有三种：'r'只读模式，'w'写入模式，'r+'读取与写入，'a'附加模式
# Python将自动创建文件，但如果文件已存在，Python将在返回文件对象前清空该文件，即覆盖原文件
with open('D:/Programs/write.txt', 'w') as file_object:
    file_object.write('Hello, world!')

# Python只能以字符串形式写入文件，如果要写入例如数值必须先转换成字符串 str()
# 在.write中也可以添加换行符\n，制表符\t等来排版文字
# 'a'为添加模式，不会覆盖原文件，会在文件末尾继续写入内容

# 方法.split()可以生成一个列表，包含文本中所有的单词，列表的长度即为单词数
example = 'Hello, world!'
words = example.split()
print(len(words))

# json模块可以将简单的Python数据结构存储到文件中
# 当程序再次运行时，加载该文件中存储的数据
# 也可以利用json在Python程序之间分享数据
import json

# 函数json.dump('data', 'filename')
numbers = [1, 1, 4, 5, 1, 4]
filepath = 'D:/Programs/Python/numbers.json'
with open(filepath, 'w') as file_object:
    json.dump(numbers, file_object)

# 使用json.load()将文件读取到内存中
with open(filepath) as file_object:
    another_numbers = json.load(file_object)

print(numbers)
print(another_numbers)

# 除了json，还可以使用pickle模块
# pickle模块是Python提供的一种序列化工具，可以将Python对象保存到文件中，并在需要时将其加载回来

import pickle

# 要存储的字典对象
data = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York',
    'is_student': False,
    'scores': [85, 92, 78]
}

# 文件路径
file_path = 'data.pkl'

# 将对象存储到文件中
with open(file_path, 'wb') as file: # wb为二进制写入模式
    pickle.dump(data, file)
    print(f"Data has been successfully stored in {file_path}")

# 从文件中加载对象
with open(file_path, 'rb') as file:
    loaded_data = pickle.load(file)
    print("Data loaded from file:")
    print(loaded_data)