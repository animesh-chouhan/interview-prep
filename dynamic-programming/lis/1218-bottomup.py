class Solution:
    def longestSubsequence(self, arr: list[int], difference: int) -> int:
        dp = [-1] * len(arr)

        for i in range(len(arr)):
            dp[i] = 1 + max(
                [dp[k] for k in range(0, i) if arr[i] - arr[k] == difference],
                default=0,
            )
        print(dp)
        return max(dp)


s = Solution()
print(s.longestSubsequence(arr=[1, 5, 7, 8, 5, 3, 4, 2, 1], difference=-2))
