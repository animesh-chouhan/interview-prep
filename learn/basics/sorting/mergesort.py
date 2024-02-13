from time import perf_counter


def merge(a, b):
    ret = []
    inf = float("inf")
    a.append(inf)
    b.append(inf)
    i = 0
    j = 0
    while not (a[i] == inf and b[j] == inf):
        # print(i, j)
        if a[i] <= b[j]:
            ret.append(a[i])
            i += 1
        else:
            ret.append(b[j])
            j += 1
    return ret


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    return merge(merge_sort(nums[:mid]), merge_sort(nums[mid:]))


a = [3, 5, 7, 8, 10]
b = []
print(merge(a, b))

nums = list(reversed(range(10)))
assert merge_sort(nums) == sorted(nums)
print(merge_sort(nums))

nums = list(reversed(range(100000)))
start = perf_counter()
merge_sort(nums)
# sorted(nums)
print(f"Time taken: {perf_counter() - start}")
