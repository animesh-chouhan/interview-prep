from collections import Counter, defaultdict


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        c = Counter(nums)
        # print(c.most_common(k))
        return [e[0] for e in c.most_common(k)]


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        h = defaultdict(int)
        for num in nums:
            h[num] += 1
        return [
            e[0] for e in sorted(h.items(), key=lambda item: item[1], reverse=True)
        ][:k]


s = Solution()
print(s.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
