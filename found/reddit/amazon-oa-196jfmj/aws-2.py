# https://www.reddit.com/r/leetcode/comments/196jfmj/amazon_oa/
from time import perf_counter


def reverse_operations(s: str):
    revs = s[::-1]
    # if s == revs:
    #     return 0
    for i in range(1, len(s) + 1):
        if revs[:i] not in s:
            i -= 1
            break
    # print(i)
    # print(revs[:i])
    return len(s) - i


def reverse_operations(s: str):
    revs = s[::-1]
    i = 0
    j = 0
    change = 0
    while i < len(s) and j < len(s):
        if s[i] == revs[j]:
            i += 1
            j += 1
        else:
            change += 1
            i += 1
    return change


def reverse_operations(s: str):
    i = 0
    j = len(s) - 1
    change = 0
    while i < len(s) and j >= 0:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            change += 1
            i += 1
    return change


# def reverse_operations(s: str):
#     revs = s[::-1]
#     # if s == revs:
#     #     return 0

#     i = 0
#     j = 0from time import perf_counterstart = perf_counter()for i in range(10000000):test = bin(i)[2:]reverse_operations(test)print(f"Time taken: {perf_counter()-start}s")
#     change = 0
#     while i < len(s) and j < len(s):
#         if s[i] == revs[j]:
#             i += 1
#             j += 1
#         else:
#             to_skip = s[i:].find(revs[j])
#             if to_skip == -1:
#                 change += len(s) - i
#                 break
#             change += to_skip
#             i += to_skip
#     return change


def reverse_operations(s: str):
    i = 0
    j = len(s) - 1
    change = 0
    while i < len(s) and j >= 0:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            to_skip = s[i:].find(s[j])
            if to_skip == -1:
                change += len(s) - i
                break
            change += to_skip
            i += to_skip
    return change


def fun(s):
    i = len(s) - 1
    j = 0
    count = 0
    while j < len(s):
        while j < len(s) and s[j] != s[i]:
            j += 1
            count += 1
        j += 1
        i -= 1
    return count


s = "0100110"
s = "01011"
# s = "111000010"
print(reverse_operations(s))
# print(fun(s))

# for i in range(100000):
#     test = bin(i)[2:]
#     print(test)
#     out1 = reverse_operations(test)
#     out2 = fun(test)
#     print(out1, out2)
#     assert out1 == out2

start = perf_counter()
for i in range(10000000):
    test = bin(i)[2:]
    reverse_operations(test)

print(f"Time taken: {perf_counter()-start}s")


def change_operations(s: str, t: str):
    i = 0
    j = 0
    change = 0
    while i < len(s) and j < len(s):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            change += 1
            i += 1
    return change
