from collections import Counter


class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        c = Counter("".join(words))
        len_words = len(words)
        for v in c.values():
            if v % len_words != 0:
                return False
        return True


s = Solution()
print(s.makeEqual(words=["abc", "aabc", "bc"]))
