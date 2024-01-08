from collections import Counter


class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        n = len(grid)
        nums = list(range(1, n * n + 1))
        for row in grid:
            for num in row:
                nums.append(num)

        # print(nums)
        ret = [0, 0]
        counter = Counter(nums)
        for k, v in counter.items():
            if v == 1:
                ret[1] = k
            if v == 3:
                ret[0] = k
        print(ret)
        return ret


s = Solution()
s.findMissingAndRepeatedValues(grid=[[1, 3], [2, 2]])
s.findMissingAndRepeatedValues(grid=[[9, 1, 7], [8, 9, 2], [3, 4, 6]])
