class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        lengths = []
        for i, c in enumerate(s):
            last_i = s[-1:i:-1].find(c)
            print(i, last_i)
            if last_i == -1:
                lengths.append(last_i)
            else:
                lengths.append(len(s) - last_i - 1 - i - 1)

        print(lengths)
        return max(lengths)


s = Solution()
s.maxLengthBetweenEqualCharacters(s="abcba")
