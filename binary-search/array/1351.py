def pos_zero(nums):
    l = 0
    r = len(nums)
    while l < r:
        mid = (l + r) // 2
        if nums[mid] >= 0:
            l = mid + 1
        else:
            r = mid

    return l


class Solution:
    def countNegatives(self, grid) -> int:
        count = 0
        for nums in grid:
            count += len(nums) - pos_zero(nums)

        return count
        return sum([len(nums) - pos_zero(nums) for nums in grid])


print(pos_zero([4, 3, 2, -1]))
print(pos_zero([4, 3, 2, 1]))
print(pos_zero([4, 3, 2, 1, 0, 0, 0]))
print(pos_zero([4, 3, 2, 1, 0, 0, -1, -2]))
