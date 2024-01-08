class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        print(nums)
        len_nums = len(nums)
        sol = [1] * len_nums
        pre = 1
        post = 1

        for i in range(1, len_nums):
            pre *= nums[i - 1]
            sol[i] *= pre
            post *= nums[len_nums - i]
            sol[len_nums - i - 1] *= post

        print(sol)
        return sol


s = Solution()
s.productExceptSelf([1, 2, 3, 4])
