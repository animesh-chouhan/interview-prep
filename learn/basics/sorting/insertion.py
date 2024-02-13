from time import perf_counter
from bisect import bisect


# TC: O(n^2)
# SC: O(n)
def insort_naive(nums):
    ret = [nums[0]]
    for i in range(1, len(nums)):
        j = 0
        while j < len(ret):
            if ret[j] > nums[i]:
                break
            j += 1
        ret.insert(j, nums[i])
    return ret


# TC: O(n^2) because of insert
# SC: O(n)
def insort_binsearch(nums):
    ret = [nums[0]]
    for i in range(1, len(nums)):
        j = bisect(ret, nums[i])
        ret.insert(j, nums[i])
    return ret


# TC: O(n^2) because of swaps
# SC: O(1)
def insort_inplace(nums):
    for i in range(1, len(nums)):
        j = i - 1
        while nums[j] > nums[j + 1] and j >= 0:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
            j -= 1
    return nums


def insort_inplace(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums


nums = list(reversed(range(10)))
assert insort_inplace(nums) == sorted(nums)
print(insort_inplace(nums))


nums = list(reversed(range(100000)))
start = perf_counter()
insort_naive(nums)
# sorted(nums)
print(f"Time taken: {perf_counter() - start}")
