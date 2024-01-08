def generate_dag(pairs):
    dag = [[] for _ in pairs]
    for i in range(len(pairs)):
        for j in range(len(pairs)):
            if pairs[j][0] > pairs[i][1]:
                dag[i].append(j)
    return dag


class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        dp = [0] * len(pairs)

        def lis(k):
            # print(k)
            dp[k] = 1 + max(
                [
                    dp[i] or lis(i)
                    for i in range(len(pairs))
                    if pairs[i][1] < pairs[k][0]
                ],
                default=0,
            )
            return dp[k]

        return max([lis(k) for k in range(len(pairs))])


s = Solution()
print(s.findLongestChain(pairs=[[1, 2], [7, 8], [4, 5]]))
