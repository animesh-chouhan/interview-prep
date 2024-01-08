def first(nums, target):
    if len(nums) == 0:
        return -1
    l = 0
    r = len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if nums[mid] >= target:
            r = mid
        else:
            l = mid + 1
    print(l, r)
    if nums[l] == target:
        return l
    else:
        return -1


def last(nums, target):
    if len(nums) == 0:
        return -1
    l = 0
    r = len(nums)
    while l < r:
        mid = (l + r) // 2
        if nums[mid] <= target:
            l = mid + 1
        else:
            r = mid
    print(l, r)
    if l > 0 and nums[l - 1] == target:
        return l - 1
    else:
        return -1


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        return [first(nums, target), last(nums, target)]


s = Solution()
print(s.searchRange(nums=[5, 7, 7, 7, 8, 8, 10, 11], target=12))
print(s.searchRange(nums=[], target=0))
