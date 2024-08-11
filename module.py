# import 
# 他终于来了！

# 模块的扩展名也是.py

import example

print(example.add(1, 2)) # 注意格式为 模块名.函数名(参数)

# 仅导入单个函数
# from 模块名 import 函数1, 函数2, 函数3
# 通过这种方法显式导入的函数调用时无需写上模块名
from example import add

print(add(1, 2))

# 为导入的模块或函数起别名 as
import example as ex
from example import add as add_numbers

# 导入模块中所有的函数
from example import *
"""注意，使用此方法导入，调用函数时无需使用句点，但可能造成命名冲突问题，所以不建议使用"""

# dir函数
# dir(模块名)
# 使用dir()函数时，返回模块定义的名称列表，如果不提供参数，则返回当前模块中定义的名称列表
# 注意，输入的模块同样是列表的一部分
print(dir())