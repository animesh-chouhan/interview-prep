from functools import lru_cache


class Solution:
    def rob(self, nums: list[int]) -> int:
        end = len(nums)

        @lru_cache
        def rob_index(n):
            if n >= end:
                return 0
            if n == end - 1 or n == end - 2:
                return nums[n]
            return max(nums[n] + rob_index(n + 2), nums[n] + rob_index(n + 3))

        return max([rob_index(i) for i in range(end)])


s = Solution()
print(s.rob([1, 2, 3, 1]))
print(s.rob([2, 7, 9, 3, 1]))
print(s.rob([9, 1, 9, 12]))
