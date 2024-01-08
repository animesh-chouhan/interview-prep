import time
from functools import lru_cache


def climb(n):
    prev = 1
    curr = 1
    for i in range(2, n + 1):
        temp = curr
        curr += prev
        prev = temp

    return curr


class Solution:
    def climbStairs(self, n: int) -> int:
        steps = climb(n)
        return steps


start = time.perf_counter()
s = Solution()
n = 200
print(s.climbStairs(n))
print(f"Time taken {n}: {time.perf_counter() - start}s")
