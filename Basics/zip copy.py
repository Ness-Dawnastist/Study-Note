# zip() 函数是 Python 内置函数之一，用于将多个可迭代对象（如列表、元组、集合）中的元素配对，返回一个迭代器，生成由对应元素组成的元组
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

zipped = zip(list1, list2)
print(list(zipped))

"""
注意，zip()返回一个迭代器，在上面list(zipped)时已经遍历完毕，即内容已经被消耗
所以此时为空，下面的dict2也会是一个空字典
解决方法是重新生成迭代器或是用一个变量来储存zip()的返回值
"""

# 组装成字典
dict1 = dict(zip(list1, list2))
dict2 = dict(zipped)
print(dict1)
print(dict2)