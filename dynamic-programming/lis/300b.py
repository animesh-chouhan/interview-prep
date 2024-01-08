class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        lis = [0] * len(nums)
        for k in range(len(nums)):
            lis[k] = 1 + max(
                [lis[i] for i in range(0, k) if nums[i] < nums[k]], default=0
            )
        print(lis)
        return max(lis)


s = Solution()
print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
