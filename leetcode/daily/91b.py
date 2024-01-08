import time
from functools import lru_cache


@lru_cache
def decode(s):
    if s[0] == "0":
        return 0
    if len(s) < 2:
        return 1
    elif len(s) == 2:
        if s == "10" or s == "20":
            return 1
        elif 11 <= int(s) <= 26:
            return 2
        elif s[1] == "0":
            return 0
        else:
            return 1

    else:
        a = decode(s[1:])
        if int(s[:2]) <= 26:
            b = decode(s[2:])
        else:
            b = 0

        return a + b


class Solution:
    def numDecodings(self, s: str) -> int:
        return decode(s)


s = Solution()
print(s.numDecodings("11106"))
print(s.numDecodings("06"))
print(s.numDecodings("60"))
print(s.numDecodings("620"))
print(s.numDecodings("3123"))
print(s.numDecodings("123123"))
