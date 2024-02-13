# CSES book page 21
import functools


# O(n^3)
def max_subarray(nums):
    poss = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            poss.append(sum(nums[i:j]))

    return max(poss)


# O(n^2) Calculating the sum in the same loop
def max_subarray(nums):
    poss = []
    for i in range(len(nums)):
        sum = 0
        for j in range(i, len(nums)):
            sum += nums[j]
            poss.append(sum)

    return max(poss)


# O(n) recursive
def max_subarray(nums):
    @functools.cache
    def max_sub_idx(i):
        if i < 0:
            return 0
        return max(nums[i], max_sub_idx(i - 1) + nums[i])

    return max(max_sub_idx(i) for i in range(len(nums)))


# O(n) iterative dp
def max_subarray(nums):
    # Max sum ending at index i
    max_idx = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        max_idx[i] = max(nums[i], max_idx[i - 1] + nums[i])

    return max(max_idx)


# O(n) Kadane's algo: memory efficient iterative dp
def max_subarray(nums):
    max_sum = 0
    curr_sum = 0
    for i in range(len(nums)):
        curr_sum = max(nums[i], curr_sum + nums[i])
        max_sum = max(max_sum, curr_sum)

    return max_sum


nums = [-1, 2, 4, -3, 5, 2, -5, 2]
print(max_subarray(nums))
