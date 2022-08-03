# 非递归思想，使用循环语句，不断累加
def sum1(start, end):
    accumulator = 0
    for n in range(start, end + 1):
        accumulator += n
    return accumulator


result = sum1(1, 100)
print("Non-Recursive:", result)

# 请Python"忘掉"上面那个sum函数
del sum1

# 递归思想，使用递归函数的自然实现


def sum1(start, end):
    if start < end:
        return start + sum1(start+1, end)
    else:
        return end  # 或return start


result = sum1(1, 100)
print("Recursive:", result)
