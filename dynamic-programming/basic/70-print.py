import time
from functools import lru_cache


@lru_cache
def climb(n):
    if n == 1:
        return [[1]]
    elif n == 2:
        return [[1, 1], [2]]
    else:
        a = [[1] + i for i in climb(n - 1)]
        b = [[2] + i for i in climb(n - 2)]
        return a + b


class Solution:
    def climbStairs(self, n: int) -> int:
        steps = climb(n)
        print(climb.cache_info())
        # print(steps)
        return len(steps)


start = time.perf_counter()
s = Solution()
n = 25
print(s.climbStairs(n))
print(f"Time taken {n}: {time.perf_counter() - start}s")
