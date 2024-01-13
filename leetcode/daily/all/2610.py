from collections import Counter, defaultdict


class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        c = Counter(nums)
        freq = c.most_common()
        ret = [[] for _ in range(freq[0][1])]
        for f in freq:
            for i in range(f[1]):
                ret[i].append(f[0])

        return ret


class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        c = Counter(nums)
        ret = []
        for k, v in c.items():
            ret.extend([[] for _ in range(v - len(ret))])
            for i in range(v):
                ret[i].append(k)

        return ret


class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        c = defaultdict(int)
        ret = []
        for num in nums:
            c[num] += 1
            if c[num] > len(ret):
                ret.append([])
            ret[c[num] - 1].append(num)

        return ret


s = Solution()
print(s.findMatrix(nums=[1, 3, 4, 1, 2, 3, 1]))
