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
            poss = []
            for i in range(k, 0, -1):
                new_target = target - i
                rem_n = n - 1
                if new_target >= 0:
                    if rem_n * k < new_target:
                        p = 0
                    elif rem_n * k == new_target:
                        p = 1
                    elif new_target < rem_n:
                        p = 0
                    elif new_target == rem_n:
                        p = 1
                    else:
                        p = throw(n - 1, k, target - i)
                else:
                    p = 0
                poss.append(p)
            return sum(poss)

    else:
        return 0


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        ret = throw(n, k, target)
        # print(throw.cache_info())
        return ret % (7 + pow(10, 9))


s = Solution()
print(s.numRollsToTarget(n=1, k=6, target=3))
print(s.numRollsToTarget(n=2, k=6, target=7))
print(s.numRollsToTarget(n=30, k=30, target=500))
