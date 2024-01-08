import time

start_time = time.perf_counter()


def is_palindrome(num):
    list_n = list(str(num))
    trans = list_n[:]
    trans_len = len(trans)
    for i in range(trans_len // 2):
        if trans[trans_len - i - 1] != trans[i]:
            return False
    return True


for _ in range(1000000):
    is_palindrome(123456789)
    is_palindrome(123454321)

print(time.perf_counter() - start_time)

# print(is_palindrome(123456789))
# print(is_palindrome(123454321))
# print(is_palindrome(9))
# print(is_palindrome(1221))
