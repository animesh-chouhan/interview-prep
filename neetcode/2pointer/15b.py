class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ret = set()

        def two_sum(i):
            j = i + 1
            k = len(nums) - 1
            target = -nums[i]
            while j < k:
                print(j, k)
                s = nums[j] + nums[k]
                if s == target:
                    ret.add((nums[i], nums[j], nums[k]))
                    k -= 1
                    j += 1
                elif s > target:
                    k -= 1
                else:
                    j += 1

        for i in range(len(nums)):
            two_sum(i)
        return [list(item) for item in ret]


s = Solution()
s.threeSum([-1, 0, 1, 2, -1, -4])
