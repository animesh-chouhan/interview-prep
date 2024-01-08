from functools import lru_cache


@lru_cache(None)
def throw(n, k, target):
    # print(n, k, target)

    if n < 0:
        return 0

    if target == 0:
        if n == 0:
            return 1
        elif n > 0:
            return 0
    elif target > 0:
        if n == 0:
            return 0
        elif n > 0:
            if target > n * k:
                return 0
            elif target == n * k:
                return 1
            else:
                return sum(
                    [
                        throw(n - 1, k, target - i)
                        for i in range(1, k + 1)
                        if (target - i >= 0) and ((n - 1) * k >= (target - i))
                    ]
                )
    else:
        return 0


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        return throw(n, k, target) % (7 + pow(10, 9))


s = Solution()
print(s.numRollsToTarget(n=1, k=6, target=3))
print(s.numRollsToTarget(n=2, k=6, target=7))
print(s.numRollsToTarget(n=30, k=30, target=500))
