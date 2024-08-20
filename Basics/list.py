# 在Python中，序列是一个用于存储多个值的连续空间，每个值都对应一个整数标号，称为索引
# 所有序列都可以使用如下操作符/函数
# in
# not in
# len()
# max()
# min()
# .index(element) 序列中第一次出现element时的位置
# .count(element) 序列中出现element的总次数
# Python中的序列有列表，元组，字典和集合，本页为列表

# 列表是动态的，随时可以增删元素，其中可以储存不同种任意类型的数据
list1 = [1, 2, 3, 4, 5]

# 在末尾添加元素 .append(element)
list1.append(6)
print(list1)

# 插入元素,将插入元素后面的元素右移一格 .insert(index, element)
list1.insert(0, 0)
print(list1)

# 删除元素
# 按索引删除元素 del list[index]
del list1[-1]
print(list1)

# 弹出元素 .pop(index)
# 弹出的元素可以用变量接收
popped_element = list1.pop() # 括号内为索引，默认为最后一个元素
print(str(popped_element))
print(list1)

# 按值删除元素 .remove(element)
list1.remove(0) #注意括号内是元素的值而不是索引
print(list1)
# 注意.remove仅能删除第一个匹配的元素

# 排序元素 .sort()
list2 = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
list2.sort()
print(list2)

# 反向排序元素 .sort(reverse=True)
list2.sort(reverse=True)
print(list2)

# 临时排序元素 sorted()
list3 = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
print(sorted(list3))
print(list3)

# 临时反向排序，括号内的参数用逗号隔开
print(sorted(list3, reverse=True))
# 括号内的参数顺序不能有误，例如sorted函数
# sorted(iterable, key=None, reverse=False)

# key参数的用法
list4 = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]
print(sorted(list4, key=abs))

# 反转列表 .reverse()
list4.reverse()
print(list4)
"""注意reverse()是没有返回值的(返回None)，所以如果print(list4.reverse())则会输出None"""

# 列表长度 len()
print(len(list4))

# 遍历列表的三种方式
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. for循环
for number in number_list:
    print(number)
# 此时变量number仍然存在，且值为10
# 可使用del来删除变量
del number

# 2. 索引循环
for i in range(len(number_list)): # range(10)返回0-9的迭代器
    print(number_list[i])

# 3. 枚举循环
for index, item in enumerate(number_list):
    print(index, item)
"""注意此处的index是序号而不是索引，也是默认从0开始的，如果不想从0开始，需要指定start参数"""

for index, item in enumerate(number_list, start=1):
    print(index, item)
"""也可以只打印item，省略序号"""

# 列表生成式
# range(start, stop, step)
for number in range(1, 7, 2): #range函数顾头不顾尾，所以仅会输出1,3,5
    print(number)

# 条件生成式
list9 = [x for x in range(1, 11) if x % 2 == 0]
print(list9)

# 创建矩阵
matrix = [[j for j in range(8)] for i in range(8)] 

# 按照规则创建列表 list()
odd_numbers = list(range(1, 11, 2)) 
# 注意list为关键词之一，但是其可以用作变量名，如之前已经用过list作为变量名则不可再使用list()函数
print(odd_numbers)

# 简单数学计算
print(min(list4))
print(max(list4))
print(sum(list4))

# 列表解析
squares = [value**2 for value in range(1, 11)]
print(squares)
# 本质就是将给变量赋值与插入到列表中合成为一行代码

# 列表切片 list[start:stop]
print(list4[2:6]) # 注意list4[6]不包含在内，即顾头不顾尾
# 输出如最后三个元素时，使用
print(list4[-3:])

# 遍历切片
for value in list4[2:6]: # 注意list4[6]不包含在内
    print(value)

# 列表复制
list5 = [1, 2, 3, 4, 5]
list6 = list5[:] # 必须使用全切片的方法，否则会复制引用
print(list6)

list7 = list5 # 这是复制引用(浅复制)，即list7和list5指向同一个列表

# 或者使用 .copy()
list8 = list5.copy()
print(list8)