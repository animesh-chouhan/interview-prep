from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cs = Counter(s)
        ts = Counter(t)
        cs.subtract(ts)
        # print(+cs)

        return (+cs).total()


s = Solution()
print(s.minSteps(s="bab", t="aba"))
print(s.minSteps(s="leetcode", t="practice"))
print(s.minSteps("asd", "hjk"))
print(s.minSteps(s="anagram", t="mangaar"))
