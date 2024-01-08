class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        count = 0
        for i in range(len(g)):
            for j in range(len(s)):
                if s[j] >= g[i]:
                    count += 1
                    s.pop(j)
                    break

        return count


s = Solution()
print(s.findContentChildren(g=[1, 2, 3], s=[1, 1]))
print(s.findContentChildren(g=[1, 2], s=[1, 2, 3]))
