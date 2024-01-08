from collections import Counter


# def delete(nums, index):
#     # print(nums, index)
#     num = nums[index]
#     if not nums:
#         return 0
#     new_nums = [
#         n for i, n in enumerate(nums) if n not in [num - 1, num + 1] and i != index
#     ]
#     print(9, num, new_nums)
#     if new_nums:
#         a = [delete(new_nums, i) for i in range(len(new_nums))]
#         print(12, a, len(new_nums))
#         return [num + delete(new_nums, i) for i in range(len(new_nums))]
#     else:
#         print(14, [num] * len(nums))
#         return num


def delete(counter, total, points=0):
    counter = +counter
    if counter.total() == 0:
        total.append(points)
    points_added = 0
    for num in counter:
        temp = +counter
        points_added = num * temp[num]
        temp[num] = 0
        # if temp[num - 1] == 0 and temp[num + 1] == 0:
        #     continue
        temp[num - 1] = 0
        temp[num + 1] = 0
        delete(temp, total, points + points_added)


class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        total = []
        delete(Counter(nums), total)
        # print(total)
        return max(total)


s = Solution()
print(s.deleteAndEarn(nums=[3, 4, 2]))
print(s.deleteAndEarn(nums=[2, 2, 3, 3, 3, 4]))
print(s.deleteAndEarn([3, 7, 10, 5, 2, 4, 8, 9, 9, 4, 9, 2, 6, 4, 6, 5, 4, 7, 6, 10]))
print(s.deleteAndEarn([1, 1, 2, 2, 3, 5, 5, 7, 8, 8, 9]))
