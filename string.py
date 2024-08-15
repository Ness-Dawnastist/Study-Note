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
# 格式化字符串通常用于更好地连接各种类型的数据
# 1.占位符
# %s 字符串 %d 十进制整数 %f 浮点数
name = "Ness Dawnastist"
age = 18
score = 101.0000
print("名字：%s\n年龄：%d\n成绩：%f" % (name, age, score))
# 使用%s %d %f直接替换字符串，然后在字符串外面加上一个%，再跟一个元组，元组中是按顺序排列的要替换的字符串
# 注意到输出的成绩是101.000000，在%f的%后面加上.4来设置小数位数为4
print("名字：%s\n年龄：%d\n成绩：%.4f" % (name, age, score))

# 2.f-string
print(f"名字：{name}\n年龄：{age}\n成绩：{score:.4f}")
# 在字符串前面加上一个f，在变量后面加上:.4f来设置小数位数为4

# 3.format()方法
print("姓名：{0}\n年龄：{1}\n成绩：{2:.4f}".format(name, age, score))
# 其中的0，1，2相当于后面元组的索引

# 格式化字符串格式
"""
: 引导符号
填充 填充单个字符
< > ^ 左对齐，右对齐，居中对齐
宽度
, 数字千位分隔符
. 精度 浮点数小数部分的精度或字符串的最大输出长度
类型 b二进制 d十进制 o八进制 x十六进制 X十六进制  e科学计数法 E科学计数法 f精度 %百分数
使用类型之前需要先有.
以上符号最好是按顺序写
"""

name = 'Ness Dawnastist'
print('{0:*^20}'.format(name)) # 左对齐，长度20，空白用*填充

# 复习：居中对齐也可以用.center
print(name.center(20, '*'))

print('{0:*^20,.2f}'.format(1234.56789)) # *填充，居中，长度20，千位分隔，小数点后两位

print('{0:*<20.5}'.format(name)) # 字符串只显示5个字符

print('{0:*<20b}\n{0:*<20d}\n{0:*<20o}\n{0:*<20x}'.format(123))
print('{0:.2f}\n{0:.2e}\n{0:.2E}\n{0:.2%}'.format(3.14159))

# 字符串的编码与解码
str1 = '你永远是中国人'

# 编码即为 str --> bytes
print(str1.encode(encoding='utf-8',errors='strict'))

# 常用utf-8或gbk编码格式，utf-8中一个中文占3个字符，gbk中占2个字符
# errors 参数如下：
# strict 默认值，如果出现编码错误，则抛出UnicodeEncodeError异常
# ignore 忽略编码错误
# replace 替换编码错误，用?代替

# 解码即为 bytes --> str
print(bytes.decode(str1.encode(encoding='utf-8',errors='strict'),encoding='utf-8',errors='strict'))

# 字符串验证
# 下列函数会返回布尔值，多用于检测用户输入的合法性
name = 'Ness Dawnastist'
# name.isdigit() 是否都为阿拉伯数字
# name.isnumeric() 是否都为数字（可以是各种数字例如罗马数字，中文数字等，甚至是大写汉字）
# name.isalpha() 是否都为字母（包含中文字符）
# name.isalnum() 是否都为字母或数字（包含中文字符）
# name.isupper() 是否都为大写字母
# name.islower() 是否都为小写字母
# name.istitle() 是否都为标题格式
# name.isspace() 是否都为空白字符（空格,\n,\t等）
# name.isdecimal() 是否都为十进制数字
# name.isidentifier() 是否为合法的标识符
# 还有很多.is什么什么的方法

# 字符串拼接
# 1.+
name1 = 'Ness'
name2 = 'Dawnastist'
print(name1 + ' ' + name2)

# 2.join
print(' '.join([name1, name2]))
# .join前面的是拼接字符，此处为空格

# 3.format
print('{} {}'.format(name1, name2))

# 4.直接拼接
print('Ness'' ''Dawnastist') # 这多少有点那个大病了

# 5.占位符
print('%s %s' % (name1, name2))

# 6.f-string
print(f'{name1} {name2}')

# 7.这样也行
print(name1,name2) # 输出仍为Ness Dawnastist,因为sep参数用了默认值' '

# 字符串去重
# 1.循环not in
name = 'Ness Dawnastist'
new_name = ''
for i in name:
    if i not in new_name:
        new_name += i
print(new_name)

# 2.索引循环
name = 'Ness Dawnastist'
new_name = ''
for i in range(len(name)):
    if name[i] not in new_name:
        new_name += name[i]
print(new_name)

# 3.集合
name = 'Ness Dawnastist'
checkset = set(name)
checklist = list(checkset)
checklist.sort(key=name.index)
print(''.join(checklist))