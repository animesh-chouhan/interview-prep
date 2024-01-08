def binary_search_rec(l, r, nums, target):
    if l > r:
        return -1
    mid = (l + r) // 2
    if nums[mid] > target:
        return binary_search_rec(l, mid - 1, nums, target)
    elif nums[mid] < target:
        return binary_search_rec(mid + 1, r, nums, target)
    else:
        return mid


def binary_search_loop(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] > target:
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1
        else:
            return mid

    return -1


nums = [1, 3, 4, 7, 9, 12, 15]
print(binary_search_rec(0, len(nums) - 1, nums, 16))
print(binary_search_loop(nums, 15))
