# if语句
# if 条件1:
#     代码块1
# elif 条件2:
#     代码块2
# else:
#     代码块3
# if的嵌套就不必多说了，注意缩进即可

gender_of_ness = "female"
if gender_of_ness == "male":
    print("Ness是下头男")
elif gender_of_ness == "female":
    print("Ness是可爱女孩子")
else:
    print("武装直升机")

# 检查多个条件
# 与and 或or 非not
# 而C++中是 && || !

if gender_of_ness == "male" or gender_of_ness == "female":
    print("Ness是正常人")

# 检查特定值是否包含在列表中
# 使用成员运算符 in 和 not in
a = 1
list1 = [2, 3, 4, 5]
if a not in list1:
    print("a不在列表中")
else:
    print("a在列表中")

# 与C++不同，Python中的布尔值用True和False表示，而不是1和0
print(1==1) # 输出True

# 注意Python中可以连着比较，如下
b = 5
if 1 < b < 3:
    print("b在1和3之间")
else:
    print("b不在1和3之间")

# 检查列表是否含有元素
list2 = []
if list2:
    print("列表不为空")
elif not list2:
    print("列表为空")

# 条件表达式 value = condition if True else value
a = 10
b = 5
max = a if a > b else b
print(max)