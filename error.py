# 异常是一种特殊对象，如果未用try模块进行处理，程序将停止并显示traceback
# try模块
try:
    # 尝试执行的代码
    print(1/0)
except ZeroDivisionError:
    # 当上面的代码抛出except后面的类型的异常时，这里会被执行
    # 可以选择性地捕获并处理特定类型的异常
    print("除数不能为0")
except Exception:
    # 捕获所有其他未被前面except处理的异常
    # 这是一个通用的异常处理，应谨慎使用
    print("发生异常")
else:
    # 如果try块没有抛出任何异常，此段代码将会被执行
    print("没有发生异常")
finally:
    # 不管是否发生异常，此段代码都会被执行
    # 通常用于清理工作，如关闭文件、释放资源等
    print("清理工作")

# 如果希望出现错误时程序一声不吭，可以在except代码块中使用pass语句
try:
    print(1/0)
except ZeroDivisionError:
    pass