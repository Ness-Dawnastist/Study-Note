# while
# while 条件:
#     语句
# else:
#     语句
# 当循环正常退出时，执行一次else语句
a = 'y'
while a == 'y':
    a = input('Ness是可爱女孩子吗?y/n')
    if a == 'y':
        print('好耶')
    else:
        print('You are dead.')
        break

else: print('Good')