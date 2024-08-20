# 字典是一系列无序的键-值对，键值对用冒号分隔，不同键值对之间用逗号分隔，键不能重复，但值可以重复
# 字典用大括号括起来，类似于C++中的结构体
"""任何对象都可以作为值，但只有不可变数据类型能够作为键"""

students = {'1001': '张三', '1002': '李四', '1003': '王五'}

# 字典的创建
# 1. 使用大括号创建字典
students = {'1001': '张三', '1002': '李四', '1003': '王五'}

# 2. 使用dict()与zip()函数创建字典
list1 = ['1001', '1002', '1003']
list2 = ['张三', '李四', '王五']

zipobj = zip(list1, list2)
students = dict(zipobj)

# print(zipobj) --> <zip object at 0x000001F853BE1700> 这是一个zip对象
# 如果转换成列表 print(list(zipobj)) --> [('1001', '张三'), ('1002', '李四'), ('1003', '王五')] 是一个元组列表

# 3. 使用参数创建字典
students = dict(s1001='张三',s1002='李四',s1003='王五') # 注意这里的参数需符合命名规范，不能以数字开头
print(students)

# 字典中的最值
print(max(students)) # 输出s1003，即输出值最大的键
print(min(students)) # 输出s1001，即输出值最小的键
print(len(students)) # 输出键值对的个数

# 字典中元素的访问[key]或.get(key)
print(students['s1001'])
print(students.get('s1001'))
# .get(key)可以指定默认值，防止直接访问的方式在键不存在时报错，默认值默认为None
print(students.get('s1004', '该学生不存在'))

# 遍历字典
# 整体输出（元组)
for item in students.items():
    print(item)

# 分别输出
for key, value in students.items(): # 方法.items()返回一个元组列表
    print(key, '-->' ,value)

# 仅遍历所有键
for key in students.keys(): # 方法.keys()返回一个键的列表
    print(key)

# 仅遍历所有值
for value in students.values(): # 方法.values()返回一个值的列表
    print(value)

# 获取键/值/键值对的列表/元组
keys = students.keys()
print(keys) # 输出 dict_keys(['s1001', 's1002', 's1003'])
print(tuple(keys)) # 输出 ('s1001', 's1002', 's1003')

items = students.items()
print(items) # 输出 dict_items([('s1001', '张三'), ('s1002', '李四'), ('s1003', '王五')])
print(list(items)) # 输出 [('s1001', '张三'), ('s1002', '李四'), ('s1003', '王五')]

# 也可以将上述元组列表转为字典
new_dict = dict(items)
print(new_dict)

# 如果想要按某种顺序遍历，可以加上方法.sorted()
for key in sorted(students.keys()):
    print(key)

# 用方法.set()来剔除重复元素
for student in set(students.values()):
    print(student) # 本例没有重复的值

# 弹出键值对
students = {'1001': '张三', '1002': '李四', '1003': '王五'}
print(students.pop('1001', '不存在')) # 当找不到键时，返回字符串'不存在'，否则返回键对应的值

# 随机弹出键值对
print(students.popitem()) # 弹出一个元组

# 清空字典
students.clear()

# 字典生成式
# 1. 规范生成 d = {key: value for item in iterable}
import random
students = {item: random.randint(1, 100) for item in range(1000, 1004)}
# 此处的item是做键，1-100的随机数做值
print(students)

# 2.映射生成 d = {key: value for key,value in zip(list1, list2)}
list1 = [1001, 1002, 1003]
list2 = ['张三', '李四', '王五']
students = {key: value for key, value in zip(list1, list2)}
print(students)

# 合并字典
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {**d1, **d2}
d4 = d1|d2
print(d3) # 字典解包
print(d4) # 字典合并