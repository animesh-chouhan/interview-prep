class Solution:
    def maxProductDifference(self, nums: list[int]) -> int:
        max_num = max(nums)
        min_num = min(nums)
        nums.remove(max_num)
        nums.remove(min_num)
        max1_num = max(nums)
        min1_num = min(nums)
        return max_num * max1_num - min_num * min1_num
