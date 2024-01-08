class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        d = {}
        for i, c in enumerate(s):
            if d.get(c):
                d[c].append(i)
            else:
                d[c] = [i]

        print(d)
        max_length = -1
        for c in d.keys():
            l = d[c]
            max_length = max(max_length, l[-1] - l[0] - 1)
        print(max_length)
        return max_length


s = Solution()
s.maxLengthBetweenEqualCharacters(s="abc")
