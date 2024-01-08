import time

start_time = time.perf_counter()


def is_palindrome(num):
    str_num = str(num)
    return str_num == str_num[::-1]


for _ in range(10000000):
    is_palindrome(123456789)
    is_palindrome(123454321)

print(time.perf_counter() - start_time)

# print(is_palindrome(123456789))
# print(is_palindrome(123454321))
# print(is_palindrome(9))
