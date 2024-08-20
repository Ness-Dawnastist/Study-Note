# Python中的lambda表达式也称为匿名函数，是一种创建小型匿名函数的方法
# 与使用def关键字定义的常规函数不同，lambda函数没有名称
# 它们通常用于需要一个小函数而不想正式定义一个函数的地方

# lambda 参数1, 参数2, ... : 表达式
add = lambda x, y: x + y
print(add(3, 5))  # 输出: 8
# 这里，lambda x, y: x + y 定义了一个匿名函数，该函数接受两个参数并返回它们的和

# 与map函数一起使用
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared) # 输出: [1, 4, 9, 16]
# map函数将lambda函数应用于列表中的每个元素

# 与filter函数一起使用
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers) # 输出: [2, 4, 6]
# filter函数使用lambda函数筛选出列表中的偶数

# 与sorted函数一起使用
points = [(1, 2), (3, 1), (5, -1), (2, 2)]
sorted_points = sorted(points, key=lambda point: point[1])
print(sorted_points) # 输出: [(5, -1), (3, 1), (1, 2), (2, 2)]
# sorted函数使用lambda函数根据元组的第二个元素对列表进行排序

# 注意lambda函数的主体只能是一个单独的表达式，不能包含多条语句

# lambda表达式还可以被用来创建新的函数对象，并且在运行时返回它们

def make_repeater(n):
    return lambda s: s*n
twice = make_repeater(2)
print(twice('word'))
print(twice(5))
"""
该函数make_repeater接受一个参数n，返回一个匿名函数
这个匿名函数接受一个参数s，并将其重复n次
代码中创建了一个名为twice的变量，它是指向make_repeater(2)返回的匿名函数的引用
最后，使用twice函数分别打印字符串'word'和整数5的重复两次的结果
"""