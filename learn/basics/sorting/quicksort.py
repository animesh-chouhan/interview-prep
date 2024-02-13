# TC: O(n) SC: O(n)
def partition(nums):
    if not nums:
        return
    key = nums[-1]
    l = []
    r = []
    for i in range(len(nums) - 1):
        num = nums[i]
        if num < key:
            l.append(num)
        else:
            r.append(num)
    ret = l + [key] + r
    return ret, len(l)


def exchange(nums, i, j):
    temp = nums[j]
    nums[j] = nums[i]
    nums[i] = temp
    return nums


# TC: O(n) SC: O(1)
def partition(nums):
    i = 0
    pivot = nums[-1]
    for j in range(len(nums) - 1):
        if nums[j] < pivot:
            # exchange i and j
            nums = exchange(nums[:], i, j)
            i += 1
    # exchange pivot with i
    nums = exchange(nums[:], i, -1)
    return nums, i


def quicksort(nums):
    if not nums:
        return nums
    nums, idx = partition(nums)
    l = quicksort(nums[:idx])
    r = quicksort(nums[idx + 1 :])
    return l + [nums[idx]] + r


# Combined quicksort
def combined_quicksort(nums):
    if not nums:
        return nums
    pivot = nums[0]
    l = [num for num in nums[1:] if num < pivot]
    r = [num for num in nums[1:] if num >= pivot]
    return quicksort(l) + [pivot] + quicksort(r)


nums = [2, 1, 6, 5, 3, 4]
# print(nums)
print(partition(nums))
print(quicksort(nums))
# print(combined_quicksort(nums))
