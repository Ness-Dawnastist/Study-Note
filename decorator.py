"""
在Python中，@ 符号用于定义装饰器（Decorators）
装饰器是一种特殊类型的函数，它们可以修改其他函数或方法的行为，而无需更改其源代码
装饰器通常用于添加功能，如日志记录、性能监控、权限检查、缓存结果等

当在函数定义之前使用 @decorator_name 形式时，
实际上是在告诉 Python 解释器在函数被定义后立即调用装饰器函数，
并将原函数作为参数传递给装饰器。装饰器函数可以执行任意的预处理，
然后返回一个新的函数对象，这个新的函数对象通常会替代原始函数的位置。
"""

# example 1
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

"""
假设我们想要创建一个装饰器，用于记录函数的输入和输出，
同时允许我们指定日志级别（例如，DEBUG 或 INFO）：
"""
# example 2

import logging
# 定义一个可以接受参数的装饰器
def log_level(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if level == 'DEBUG':
                logging.debug(f'Calling {func.__name__} with args={args}, kwargs={kwargs}')
                logging.debug(f'{func.__name__} returned {result}')
            elif level == 'INFO':
                logging.info(f'Calling {func.__name__} with args={args}, kwargs={kwargs}')
                logging.info(f'{func.__name__} returned {result}')
            return result
        return wrapper
    return decorator

# 使用装饰器
@log_level('DEBUG')
def add(a, b):
    return a + b

# 设置日志级别为 DEBUG
logging.basicConfig(level=logging.DEBUG)

# 调用函数
result = add(5, 3)
print(result)

"""
在这个例子中：

log_level 是一个高阶函数，它接受一个参数 level 并返回一个装饰器。
内部的 decorator 函数接收一个函数 func 作为参数，并返回一个包装后的函数 wrapper。
wrapper 函数负责记录输入和输出，并调用原始函数 func。
当我们使用 @log_level('DEBUG') 来装饰 add 函数时，
实际上是将 add 函数传入了由 log_level 返回的装饰器中。
最后，当调用 add 函数时，实际上是调用了经过装饰器包装后的版本。
这样，每次调用 add 函数时，都会自动记录函数的输入和输出，
而无需在函数内部显式地添加日志语句。此外，通过传递不同的参数给 log_level 装饰器，
我们可以轻松地改变日志级别。
"""