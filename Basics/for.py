for a in range(1, 5):
    print(a)

# range函数给出了队列[1, 2, 3, 4]
# range函数的第三个参数可以指定步长，例如range(1, 5, 2)会给出队列[1, 3]

# else语句只有在循环正常结束时才会执行，用break退出时，else语句块不会被执行
for a in range(1, 5, 2):
    print(a)
    break

else:
    print('exit')