import time

start_time = time.perf_counter()


def is_palindrome(num):
    rev = 0
    num_copy = num
    while num_copy > 0:
        rev = 10 * rev + num_copy % 10
        num_copy = num_copy // 10
    return num == rev


for _ in range(1000000):
    is_palindrome(123456789)
    is_palindrome(123454321)

print(time.perf_counter() - start_time)

# print(is_palindrome(123456789))
# print(is_palindrome(123454321))
# print(is_palindrome(9))
