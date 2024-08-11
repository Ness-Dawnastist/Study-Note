# 按位与 & (AND)
# 只有两个位都为 1 时，结果才为 1，否则为 0
5 & 3  # 5 的二进制是 101, 3 的二进制是 011
       # 结果是 001（二进制），即 1（十进制）

# 按位或 | (OR)
# 只要有一个位为 1，结果就为 1，否则为 0
5 | 3  # 5 的二进制是 101, 3 的二进制是 011
       # 结果是 111（二进制），即 7（十进制）

# 按位异或 ^ (XOR)
# 只有两个位有一个为 1，结果才为 1，否则为 0
5 ^ 3  # 5 的二进制是 101, 3 的二进制是 011
       # 结果是 110（二进制），即 6（十进制）

# 按位取反 ~ (NOT)
# 将每个位取反（0 变 1，1 变 0）
~5  # 5 的二进制是 0000 0101
    # 取反结果是 1111 1010（二进制），在计算机中表示为 -6（十进制）


# 左移 << (Left Shift)
# 将二进制数的位向左移动指定的位数，右边用 0 填补
5 << 1  # 5 的二进制是 101，左移一位变成 1010
        # 结果是 10（十进制）


# 右移 >> (Right Shift)
# 将二进制数的位向右移动指定的位数，左边用符号位填补（算术右移）或 0 填补（逻辑右移）
5 >> 1  # 5 的二进制是 101，右移一位变成 10
        # 结果是 2（十进制）

# 操作二进制数，可以利用掩码
num = 0b00101100

# 设置第2位为1（掩码：0b00000100）
set_mask = 0b00000100
num = num | set_mask
print(f"设置第2位为1后的结果: {bin(num)}")  # 输出: 0b00101100