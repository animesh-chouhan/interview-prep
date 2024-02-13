from bisect import bisect
from collections import defaultdict


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            try:
                j = nums[i + 1 :].index(target - nums[i]) + i + 1
                # j = nums.index(target - nums[i], i + 1)
                return [i, j]
            except ValueError:
                continue


# hashmap trading complexity with space 2pass
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        present = defaultdict(list)
        for i, num in enumerate(nums):
            present[num].append(i)

        for i, num in enumerate(nums):
            temp = present[target - num]
            # print(temp)
            if target - num == num:
                if len(temp) > 1:
                    return [temp[0], temp[1]]
            elif temp:
                return [i, temp[0]]


# hashmap trading complexity with space 2pass
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]


# hashmap trading complexity with space 1pass
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i


# # sorting and binary search
# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         snums = sorted(nums)
#         for i, num in enumerate(snums):
#             new_t = target - num
#             # print(new_t)
#             if target > num:
#                 j = bisect(snums, new_t)
#             else:
#                 j = bisect(snums, new_t)

#             # print(i, j, new_t)
#             if snums[j - 1] == new_t:
#                 return [
#                     nums.index(snums[i]),
#                     len(nums) - 1 - nums[::-1].index(snums[j - 1]),
#                 ]


s = Solution()

print(s.twoSum(nums=[2, 7, 11, 15], target=9))
print(s.twoSum(nums=[3, 3], target=6))
print(s.twoSum(nums=[3, 2, 4], target=6))
