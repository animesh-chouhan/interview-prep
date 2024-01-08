def range_num(nums, target):
    if len(nums) == 0:
        return [-1, -1]
    start_l = 0
    start_r = len(nums)
    end_l = 0
    end_r = len(nums)
    while start_l < start_r and end_l < end_r:
        # print(end_l, end_r)
        mid_start = (start_l + start_r) // 2
        mid_end = (end_l + end_r) // 2
        if nums[mid_start] >= target:
            start_r = mid_start
        else:
            start_l = mid_start + 1

        if nums[mid_end] <= target:
            end_l = mid_end + 1
        else:
            end_r = mid_end

    print(start_l, start_r)
    print(end_l, end_r)
    if (
        start_l < len(nums)
        and nums[start_l] == target
        and end_l > 0
        and nums[end_l - 1] == target
    ):
        return [start_l, end_l - 1]
    else:
        return [-1, -1]


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        return range_num(nums, target)


s = Solution()
print(s.searchRange(nums=[5, 7, 7, 7, 8, 8, 10, 11], target=11))
print(s.searchRange(nums=[2, 2], target=2))
print(s.searchRange(nums=[1, 4], target=4))
print(s.searchRange(nums=[], target=0))
