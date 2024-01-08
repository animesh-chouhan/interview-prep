from collections import Counter


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
        nums.sort()
        chunks = []
        temp = []
        for i in range(len(nums)):
            temp.append(nums[i])
            if i < len(nums) - 1 and nums[i + 1] - nums[i] <= 1:
                continue
            else:
                chunks.append(temp)
                temp = []
        # print(chunks)
        max_scores = []
        for chunk in chunks:
            print(chunk)
            total = []
            delete(Counter(chunk), total)
            # print(total)
            max_scores.append(max(total))
        return sum(max_scores)


s = Solution()
print(s.deleteAndEarn(nums=[3, 4, 2]))
print(s.deleteAndEarn(nums=[2, 2, 3, 3, 3, 4]))
print(s.deleteAndEarn([3, 7, 10, 5, 2, 4, 8, 9, 9, 4, 9, 2, 6, 4, 6, 5, 4, 7, 6, 10]))
print(s.deleteAndEarn([1, 1, 2, 2, 3, 5, 5, 7, 8, 8, 9]))
