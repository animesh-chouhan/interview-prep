class Solution:
    def longestSubsequence(self, arr: list[int], difference: int) -> int:
        dp = [-1] * len(arr)

        def lis(i):
            if dp[i] == -1:
                dp[i] = 1 + max(
                    [
                        dp[k] or lis(k)
                        for k in range(0, i)
                        if arr[i] - arr[k] == difference
                    ],
                    default=0,
                )
            return dp[i]

        return max([lis(i) for i in range(len(arr))])


s = Solution()
print(s.longestSubsequence(arr=[1, 5, 7, 8, 5, 3, 4, 2, 1], difference=-2))
