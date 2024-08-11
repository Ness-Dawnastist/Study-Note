import os

# 使用方法.getcwd()获取当前工作目录
print('当前工作目录:', os.getcwd())

# 使用方法.chdir()切换目录
# 切换到指定子目录
os.chdir('Python')
print('切换到子目录后的工作目录:', os.getcwd())

# 切换回上一级目录
os.chdir('..')
print('切换回上一级目录后的工作目录:', os.getcwd())

# with open()可以打开当前以及下级目录中有的文件
# 例如当前目录为C:\1
# 需要打开的文件为C:\1\2\example.txt
# with open('2\example.txt') as file: 即可，这里就使用了相对路径

# 如果要跳转到上一级，需要使用..
# 例如当前目录为C:\1\2\3
# 需要打开的文件为C:\1\example.txt
# with open('..\..\example.txt') as file: 即可

# 使用方法.path.join()拼接路径
current_directory = os.getcwd()
file_path = os.path.join(current_directory, 'subdir', 'example.txt')
print('文件路径:', file_path)

# 使用方法.path.exists()判断文件是否存在
if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)
else:
    print('文件不存在:', file_path)


# 使用方法.path.abspath()将相对路径转换为绝对路径

# 相对路径
relative_path = 'subdir/example.txt'

# 转换为绝对路径
absolute_path = os.path.abspath(relative_path)
print('绝对路径:', absolute_path)
