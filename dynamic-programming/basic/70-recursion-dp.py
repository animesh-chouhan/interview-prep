import time
from functools import lru_cache

cache = {}


def climb(n):
    val = cache.get(n)
    if val:
        return val
    if n == 0 or n == 1:
        return 1

    else:
        result = climb(n - 1) + climb(n - 2)
        cache[n] = result

    return cache[n]


class Solution:
    def climbStairs(self, n: int) -> int:
        steps = climb(n)
        return steps


start = time.perf_counter()
s = Solution()
n = 200
print(s.climbStairs(n))
print(f"Time taken {n}: {time.perf_counter() - start}s")
