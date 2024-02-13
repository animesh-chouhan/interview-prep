def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a

    if a > b:
        return gcd(a - b, b)
    else:
        return gcd(b - a, a)


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


print(gcd(2, 12))
