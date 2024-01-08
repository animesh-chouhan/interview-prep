import time

start_time = time.perf_counter()


def is_palindrome(num):
    list_n = list(str(num))
    trans = list_n[:]
    trans_len = len(trans)
    for i in range(trans_len // 2):
        trans[trans_len - i - 1] = trans[i]
    return list_n == trans


for _ in range(10000000):
    is_palindrome(123456789)
    is_palindrome(123454321)

print(time.perf_counter() - start_time)

# print(is_palindrome(123456789))
# print(is_palindrome(123454321))
# print(is_palindrome(9))
