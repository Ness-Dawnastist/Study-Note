# def 函数名(参数):
#     函数体

# 最简单无参无反函数
def greet():
    print("Hello World!")

# 传递实参的方法
# 位置实参
def add(a, b):
    print(a) 
    print(b)
    return a + b
print(add(1, 2)) # 1和2分别对应a和b，按照位置排序

# 关键字实参
def add(a, b):
    print(a) 
    print(b)
    return a + b
print(add(a=1, b=2)) # 在调用函数时指定将哪个值赋给哪个形参

# 默认值
def add(a=1, b=2): # 在定义函数时指定形参的默认值
    """注意这里重定义函数会导致之前的定义被覆盖"""
    print(a) 
    print(b)
    return a + b
print(add())
print(add(3, 4)) # 重新赋值即可覆盖默认值

# 注意 使用默认值时，在形参列表中必须先列出没有默认值的形参，再列出有默认值的实参
# 这让Python依然能够正确地解读位置实参

# 可选参数
def add(a, b, isPrint=False):
    if isPrint:
        print("a + b =", a + b)
    else:
        print(a + b)
add(5, 6, True)
add(5, 6)

# 返回一个字典
def build_person(first_name, last_name, age = ''):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name} 
    if age:
        person['age'] = age
    return person 

musician = build_person('jimi', 'hendrix', '27') 
print(musician)

# 将列表传递给函数，函数对形参列表做的修改就是对实参列表的修改
students = ['alice', 'bob', 'charlie']
def remove_last_student(students):
    del students[-1]
    print(students)
remove_last_student(students)
print(students)

# 如果不想对实参列表修改，应使用全切片传递
students = ['alice', 'bob', 'charlie']
def remove_last_student(students):
    del students[-1]
    print(students)
remove_last_student(students[:])
print(students)

# 传递未知个数的形参
def add_all_numbers(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total
print(add_all_numbers(1, 2, 3, 4, 5))
# 形参*numbers中的星号让Python创建一个名为numbers的空元组，并将收到的所有值都封装到这个元组中
"""
Python先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中
所以如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后
"""

# 使用任意数量的关键字实参
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)
# 形参**user_info让Python创建一个名为user_info的空字典，并将收到的所有键值对都封装到这个字典中

# 使用global语句来定义全局变量
# global 变量名

# 如果在函数中需要接受可变数量的参数，可以使用*或**前缀
def add(*args): #多出来的参数作为一个列表传入
    print(args)
    return sum(args)

print(add(1, 2, 3, 4, 5))  # 使用圆括号进行函数调用

def exam(name, age, **scores): #多出来的参数作为一个字典传入
    print(scores)

exam('zhangsan', 18, Math=100, English=90)