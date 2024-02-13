class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        # print(prefix)
        # print(suffix)
        return [prefix[i] * suffix[i] for i in range(len(nums))]


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
            j = len(nums) - i - 1
            suffix[j] = suffix[j + 1] * nums[j + 1]

        # print(prefix)
        # print(suffix)
        return [prefix[i] * suffix[i] for i in range(len(nums))]


s = Solution()
print(s.productExceptSelf(nums=[1, 2, 3, 4]))
print(s.productExceptSelf(nums=[-1, 1, 0, -3, 3]))
