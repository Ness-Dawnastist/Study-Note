# id()函数返回对象的内存地址
a = 1
b = 2
c = [1, 2, 3]
d = {'a': 1, 'b': 2}
e = d
print(id(a))
print(id(b))
print(id(c))
print(id(d))
print(id(e))

# 一般来说像e = d这样都是复制引用，两个变量指向同一个地址
# 如果想复制一份新的对象，需要使用copy()函数
f = c.copy()
print(id(f))