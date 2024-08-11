print()
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# *objects: 输出对象，对象间用空格分隔
# sep: 指定分隔符，默认为' '
# end: 指定结束符，默认为\n
# file: 输出文件，默认为sys.stdout，即标准输出（控制台）
# flush: 是否刷新缓冲区，立即刷新可以使输出立刻显示，默认为False

import time

size = 8
for i in range(size * size):

    # 清空屏幕并将光标移到左上角
    print("\033[H\033[J")

    row_to_remove = (size * size - 1 - i) // size
    col_to_remove = (size * size - 1 - i) % size
    
    for row in range(size):
        for col in range(size):
            if row > row_to_remove or (row == row_to_remove and col > col_to_remove):
                print(" ", end="")
            else:
                print(".", end="")
        print()

    time.sleep(1)