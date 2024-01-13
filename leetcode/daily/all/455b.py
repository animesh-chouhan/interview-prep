class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        count = 0
        len_g = len(g)
        for _ in range(len_g):
            max_greed = max(g)
            if s:
                max_s = max(s)
            else:
                break
            print(max_greed, max_s)
            g.remove(max_greed)
            if max_s >= max_greed:
                count += 1
                s.remove(max_s)

        return count


s = Solution()
print(s.findContentChildren(g=[1, 2, 3], s=[1, 1]))
print(s.findContentChildren(g=[1, 2], s=[1, 2, 3]))
