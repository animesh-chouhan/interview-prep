import time
from functools import lru_cache


@lru_cache
def decode(s):
    if len(s) < 2:
        return [[s]]
    elif len(s) == 2:
        return [[s[0], s[1]], [s]]

    else:
        a = [[s[0]] + i for i in decode(s[1:])]
        b = [[s[:2]] + i for i in decode(s[2:])]

        return a + b


class Solution:
    def numDecodings(self, s: str) -> int:
        decoded = decode(s)
        count = 0
        for d in decoded:
            flag = [i[0] != "0" and 1 <= int(i) <= 26 for i in d]
            if all(flag):
                count += 1

        return count


s = Solution()
print(s.numDecodings("11106"))
# print(decode("11106"))
# print(decode("111111"))


start = time.perf_counter()
s = "11111111111111111111111111111111"
decode(s)
print(f"Time taken {len(s)}: {time.perf_counter() - start}s")
