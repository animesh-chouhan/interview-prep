from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)
        k1 = set(c1.keys())
        k2 = set(c2.keys())
        v1 = sorted(c1.values())
        v2 = sorted(c2.values())
        return v1 == v2 and k1 == k2


s = Solution()
print(s.closeStrings(word1="abc", word2="bca"))
print(s.closeStrings(word1="abd", word2="bca"))
print(s.closeStrings(word1="uau", word2="ssx"))
