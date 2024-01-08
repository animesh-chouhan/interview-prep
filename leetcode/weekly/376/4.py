from collections import Counter


class Solution:
    def maxFrequencyScore(self, nums: list[int], k: int) -> int:
        counter = Counter(nums)
