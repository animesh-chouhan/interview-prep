class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        print(nums)
        len_nums = len(nums)
        sol = [1] * len_nums

        for i in range(1, len_nums):
            sol[i] *= nums[i - 1]
            sol[i] *= sol[i - 1]

        print(sol)
        post = 1
        for i in range(len_nums - 2, -1, -1):
            post *= nums[i + 1]
            sol[i] *= post

        print(sol)
        return sol


s = Solution()
s.productExceptSelf([1, 2, 3, 4])
