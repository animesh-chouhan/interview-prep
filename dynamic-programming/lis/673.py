class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        lis = [0] * len(nums)
        ways = [0] * len(nums)
        for k in range(len(nums)):
            lis[k] = 1 + max(
                [lis[i] for i in range(0, k) if nums[i] < nums[k]], default=0
            )
            ways[k] = (
                sum(
                    [
                        ways[i]
                        for i in range(0, k)
                        if nums[i] < nums[k] and lis[i] == lis[k] - 1
                    ]
                )
                or 1
            )
        print(lis)
        print(ways)
        max_lis = max(lis)
        total = 0
        for i in range(len(nums)):
            if lis[i] == max_lis:
                total += ways[i]

        return total


s = Solution()
print(s.findNumberOfLIS([1, 3, 5, 4, 7, 8, 10, 9, 11]))
print(s.findNumberOfLIS([2, 2, 2, 2, 2]))
