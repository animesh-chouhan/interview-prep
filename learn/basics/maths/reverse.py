def reverse(n):
    ret = n % 10
    n = n // 10
    while n > 0:
        ret = ret * 10 + n % 10
        n = n // 10
    return ret


n = 4564548464112
assert reverse(n) == int(str(n)[::-1])
print(reverse(n))
