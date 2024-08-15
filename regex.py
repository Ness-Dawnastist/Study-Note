import re
# 正则表达式是一种用于匹配字符串中字符组合的模式
# 常用于文本搜索、替换、验证等操作中，可以用来快速找到特定的字符串模式或提取数据

# 元字符
# ^ 匹配开始
# $ 匹配结束
# . 匹配任意字符（除\n)
# \w 匹配字母、数字、下划线
# \W 匹配非字母、数字、下划线
# \s 匹配空白字符
# \S 匹配非空白字符
# \d 匹配十进制数

# 限定符
# ?       匹配前面的字符0或1次
# +       匹配前面的字符1次或多次
# *       匹配前面的字符0次或多次
# {n}     匹配前面的字符n次
# {n,}    匹配前面的字符最少n次
# {n,m}   匹配前面的字符最少n次，最多m次

# 其他字符
# []  区间字符    匹配[]中指定的字符
# ^   排除字符    匹配不在[]中的字符
# |   选择字符    匹配|左右的字符
# \   转义字符    同Python中的转义字符
# ()  分组字符    改变限定符的作用
# [\u4e00-\u9fa5] 匹配任意一个汉字

# match函数
# re.match(pattern, string, flags=0)
# 从字符串的开始位置匹配，如起始位置匹配成功返回Match对象，匹配失败返回None
str1 = "3.14159 亻尔女子"
pattern1 = r'\d.\d+' # 这是一个模式字符串
"""书写模式字符串时最好使用原始字符串"""
# \d 匹配任意数字 \. 转义.，即匹配一个字符'.' \d+ 匹配一个或多个数字
match1 = re.match(pattern1, str1, re.I) # re.I 忽略大小写
print(match1) # 输出的span元组为找到的字符位置，match为匹配的字符

print("匹配值的起始位置：",match1.start())
print("匹配值的结束位置：",match1.end())
print("匹配区间的位置元素：",match1.span())
print("待匹配的字符串：",match1.string) # 注意string是属性而不是方法
print("匹配的数据：",match1.group())

# search函数
# re.search(pattern, string, flags=0)
# 匹配字符串中第一个匹配的值，匹配成功返回Match对象，失败返回None
str2 = "亻尔女子3.14159 亻尔女子6.28318"
pattern2 = r'\d.\d+'
match2 = re.search(pattern2, str2, re.I)
print(match2)

# findall函数
# re.findall(pattern, string, flags=0)
# 匹配所有匹配的值，返回一个列表（失败返回一个空列表）
str3 = "3.14159 亻尔女子6.28318"
pattern3 = r'\d.\d+'
match3 = re.findall(pattern3, str3, re.I)
print(match3)

# sub函数
# re.sub(pattern, repl, string, count=0, flags=0)
# 用于对指定的字串进行替换
str4 = 'Fuck you little bitch, have sex with me now.'
pattern4 = r'fuck|bitch|sex'
filtered_str4 = match4 = re.sub(pattern4, '***', str4, flags=re.I)
print(filtered_str4)

# split函数
# re.split(pattern, string, maxsplit=0, flags=0)
# 将字符串按照指定的规则拆分
str5 = 'https://www.bilibili.com/video/BV1wD4y1o7AS?p=74&spm_id_from=pageDriver&vd_source=13c324cf1221e16a0f3f3fa31baf95b6'
pattern5 = r'[/|?|&]'
splited_str5 = re.split(pattern5, str5)
print(splited_str5)