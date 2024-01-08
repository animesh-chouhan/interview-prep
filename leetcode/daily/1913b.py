class Solution:
    def maxProductDifference(self, nums) -> int:
        max_num = 0
        max1_num = 0
        min_num = float("inf")
        min1_num = float("inf")
        for num in nums:
            if num > max_num:
                max1_num = max_num
                max_num = num
            elif num > max1_num:
                max1_num = num

            if num < min_num:
                min1_num = min_num
                min_num = num
            elif num < min1_num:
                min1_num = num

        # print(max_num, max1_num)
        # print(min_num, min1_num)
        return max_num * max1_num - min_num * min1_num


s = Solution()
print(s.maxProductDifference([1, 6, 7, 5, 2, 4, 10, 6, 4]))
print(s.maxProductDifference([10, 10]))
