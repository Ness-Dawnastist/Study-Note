# repr函数可以返回对象的字符串表示，这种表示形式通常可以用来重新创建该对象
name = 123
print(type(name))
name = repr(name)
print(type(name))