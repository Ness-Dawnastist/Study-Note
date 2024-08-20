# assert语句可以检查其后面语句是否为真，如果为假则会使程序报错
def divide(a, b):
    assert b != 0, "Division by zero is not allowed" # 其后可以有提示信息
    return a / b

print(divide(10, 2))  # 结果: 5.0
print(divide(10, 0))  # 抛出 AssertionError: Division by zero is not allowed