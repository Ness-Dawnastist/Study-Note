class Dog(): # 在Python中，首字母大写的名称指的是类
    """一次模拟小狗的简单尝试"""
    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age
    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")

# 类中的函数称为方法
# 方法__init__()是一个特殊的方法，每当根据Dog类创建新实例时，Python都会自动运行它
# 形参self必不可少，且必须位于其他形参的前面
# Python在调用__init__方法创建实例时会自动传入实参self
# 它是一个指向实例本身的引用，让实例能够访问类中的属性和方法
# 以self为前缀的变量都可供类中的所有方法使用，还可以通过类的任何实例来访问这些变量
# self.name = name获取存储在形参name中的值，并将其存储到变量name中，
# 然后该变量被关联到当前创建的实例，这样可通过实例访问的变量称为属性

# 根据类创建实例
my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

# 方法__init__()并未显式地包含return语句，但Python自动返回一个表示这条小狗的实例
# 这个实例存储在变量my_dog中

# 访问属性--句点表示法
my_dog.name = 'Ness'
print(my_dog.name)

# 调用方法
my_dog.sit()

# 可以创建多个名字不同的实例，分别对其进行不同操作
# 类中的每个属性都必须有初始值，可以在方法__init__()中指定默认值或是接收参数传来的值
# 如果对某个属性指定了默认值，就无需包含提供初始值的形参
# 修改属性值可以直接通过实例访问或在类内定义方法

# 继承
# 子类继承了其父类的所有属性和方法，同时还可以定义自己的属性和方法
class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
class ElectricCar(Car): # 括号中的Car是父类
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year) # super()函数将父类与子类关联起来
        self.battery_size = 70 # 电动车特有的属性
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

# 如果父类中有方法对某个子类不适用，可以进行重写
# 即在子类中定义一个与父类中同名的方法

# 如果属性很多，则可以将部分属性单独作为一个类，即将实例用作属性
class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""
    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

class ElectricCar(Car): # 括号中的Car是父类
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year) # super()函数将父类与子类关联起来
        self.battery = Battery() # 将实例用作属性
        self.battery_size =70 # 电动车特有的属性

# Battery没有继承任何类，但是每次创建电动车实例时，都会创建一个Battery实例
# 这样之后再想给电瓶添加属性时，就不会干扰到电动车类的其他部分

# 也可以从其他文件导入类，方法与导入函数是相同的
# 还可以在模块中导入模块，具体使用的方法随实际情况而定
# Python标准库包含了许多函数和类，尽情使用吧
# 之后还将学习如何从其他地方下载外部模块
