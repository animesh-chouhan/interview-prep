class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        print(nums)
        len_nums = len(nums)
        pre = [1] * len_nums
        for i in range(1, len_nums):
            pre[i] *= nums[i - 1]
            pre[i] *= pre[i - 1]

        print(pre)

        post = [1] * len_nums
        for i in range(len_nums - 2, -1, -1):
            post[i] *= nums[i + 1]
            post[i] *= post[i + 1]

        print(post)

        sol = [1] * len_nums
        for i in range(len_nums):
            sol[i] = pre[i] * post[i]

        print(sol)
        return sol


s = Solution()
s.productExceptSelf([1, 2, 3, 4])
