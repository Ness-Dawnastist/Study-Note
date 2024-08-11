# 集合（set）是一种无序、不重复的元素集合
# 集合中只能存储不可变数据类型
# 集合与字典都是用{}来创建，当只有{}时，创建的是空字典
# 创建集合
s = {1, 2, 3, 4, 5}
t = set([3, 4, 5, 6, 7]) # set()中是一个可迭代对象

# 添加元素
s.add(6)

# 删除元素
s.remove(2)

# 清除所有元素
s.clear()

# 集合运算
union = s | t         # 并集
intersection = s & t  # 交集
difference = s - t    # 差集

# 遍历集合
# 集合没有索引，只能用for循环或者emu
s = {1, 2, 3, 4, 5}
for item in s:
    print(item)

for index, item in enumerate(s):
    print(index, item)

# 集合生成式
s = {i for i in range(1, 11) if i % 2 == 0}
print(s)