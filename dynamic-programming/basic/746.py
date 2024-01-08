class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        cache = {}
        end = len(cost)

        def climb(start):
            if start < end:
                val = cache.get(start)
                if val:
                    return val
                result = min(
                    cost[start] + climb(start + 1), cost[start] + climb(start + 2)
                )
                cache[start] = result
                return result
            else:
                return 0

        return min(climb(0), climb(1))


s = Solution()
print(s.minCostClimbingStairs(cost=[10, 15, 20]))
print(s.minCostClimbingStairs(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
