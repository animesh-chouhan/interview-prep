from collections import defaultdict


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        set_nums = set(nums)

        seq = []
        for num in nums:
            if num - 1 not in set_nums:
                count = 0
                while (num + count) in nums:
                    count += 1
                seq.append(count)
        # print(seq)
        return max(seq)


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        set_nums = set(nums)

        longest = 0
        for num in set_nums:
            if num - 1 not in set_nums:
                count = 0
                while (num + count) in set_nums:
                    count += 1
                longest = max(longest, count)
        # print(seq)
        return longest


s = Solution()
s.longestConsecutive(nums=[100, 4, 200, 1, 3, 2])
s.longestConsecutive([0, 1, 2, 4, 8, 5, 6, 7, 9, 3, 55, 88, 77, 99, 999999999])
