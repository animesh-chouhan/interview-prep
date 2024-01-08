class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        nums.sort()
        ret = [[nums[i - 1], nums[i], nums[i + 1]] for i in range(1, len(nums) - 1, 3)]

        flag = False
        for arr in ret:
            if arr[-1] - arr[0] > k:
                flag = True

        if flag:
            ret = []
            return []
        print(ret)
        return ret


s = Solution()
s.divideArray(nums=[1, 3, 4, 8, 7, 9, 3, 5, 1], k=2)
s.divideArray(nums=[1, 3, 3, 2, 7, 3], k=3)
