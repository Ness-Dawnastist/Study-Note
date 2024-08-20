# input(hint)
# input()函数接受一个参数，用于提示用户输入内容
input("输入任意字符继续：")

# 存储到变量中
name = input("请输入你的名字：")
print("你的名字是：" + name)

# 提示词可以是多行，例如
input("Hello!" + "\nPlease enter anything to continue.")
print("Great!")

# 或使用变量来存储多行字符串
prompt = "Hello!"
prompt += "\nPlease enter anything to continue." 
input(prompt)

# Python默认将输入理解成字符串，如果要输入数值，举例如下
num = input("How old are you?")
num = int(num)
if num >= 18:
    print("You are old enough to vote.")
else:
    print("Please come back in " + str(18 - num) + " years.")