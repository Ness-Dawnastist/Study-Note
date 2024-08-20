# 元组
# 元组是不可变的列表，元素个数和其值都不能修改
tuple1 = (1, 2, 3, 4, 5)

tuple2 = tuple([1, 2, 3, 4, 5])
# 使用tuple函数创建元组时，如果提供一个字符串"Ness"或者是一个列表[10, 20, 30]
# 会创建出('N', 'e', 's', 's')和(10, 20, 30)这样的元组
"""但使用tuple来创建元组时，必须提供一个序列，而不能是单独的元素，这体现了tuple函数多用于转换序列类型"""

# 遍历元组
for value in tuple1:
    print(value)

# 可以重新定义元组，即给元组变量赋值
tuple1 = (1, 2, 3, 4, 5, 6)
for value in tuple1:
    print(value)

# 如果元组只有一个元素，需要加逗号，否则会被识别为其他数据类型
tuple1 = (1,)
a = (1) # a的值为整数1
print(type(tuple1))
print(type(a))

# 元组生成式
# 元组生成式与列表不同
t = (x for x in range(5))
print(t)
"""
上述两行会生成例如 <generator object <genexpr> at 0x000001FA9057AC80>
这是一个生成器，如果要将其变为元组形式，要使用函数tuple()
"""
t = tuple(t)
print(t)

# 对于生成器中的元素，可以用__next__()方法逐一取出
t = (x for x in range(5))

print(t.__next__())
print(t.__next__())
print(t.__next__())
print(t.__next__())
print(t.__next__())
# 如果继续print会报错

# 如果对生成器中的元素进行遍历，会导致元素被取出，遍历完毕后不留下数据
t = (x for x in range(5))

for i in t:
    print(i)
t = tuple(t)
print(t) # 空元组