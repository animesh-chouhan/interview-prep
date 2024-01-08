class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        count = 0
        while i < len(nums):
            next_num = nums[i + 1]
