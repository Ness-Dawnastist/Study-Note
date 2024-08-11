# 字符串是不可变数据类型
name = "Ness Dawnastist"
name.title() # 单词首字母大写
name.upper() # 全大写
name.lower() # 全小写

name.split(sep=None) # 把字符串按照指定的分隔符进行分隔，结果为列表，默认以空格为分隔符
name.count('Ness') # 查找子字符串的个数
name.find('Ness') # 检测字串是否存在，存在返回索引，不存在返回-1
name.index('Ness') # 与find相同，但不存在时会报错
name.startswith('N') # 查询字符串是否以'N'开头
name.endswith('N') # 查询字符串是否以'N'结尾
name.replace('str1', 'str2') # 用str2替换所有的str1
# name.center(width, fillchar) # 使字符串在指定的宽度范围内居中，fillchar为填充字符
# name.join(iter) 在可迭代对象iter中的每个元素的后面都增加一个字符串name

# 删除左右指定字符，默认为空格 .lstrip() .rstrip() .strip()
favorite_language = " python "
print(favorite_language.lstrip())
print(favorite_language.rstrip())
print(favorite_language.strip())
"""注意，strip()方法会逐个删除所提供的参数中有的字符，直到遇见第一个没有提供的字符"""
str1 = "1112312312313212139123123123"
print(str1.lstrip("123")) # 输出9

# 常用转义字符
# \n 换行
# \t 制表
# \' 单引号
# \" 双引号
# \\ 反斜杠
# 原字符 r 或 R 加在字符串之前可以使所有转义字符失效

# 字符串格式化