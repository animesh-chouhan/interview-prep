class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums)
        while r > l:
            mid = (l + r) // 2
            # print(mid)
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid
        if l > 0 and nums[l - 1] == target:
            return l - 1
        else:
            return -1


s = Solution()
print(s.search(nums=[-1, 0, 3, 5, 9, 12], target=9))
print(s.search(nums=[-1, 0, 3, 5, 9, 12], target=2))
print(s.search(nums=[-1], target=2))
print(s.search(nums=[-1], target=-1))
print(s.search(nums=[-1, 2], target=-1))
print(s.search(nums=[-1, 2], target=2))
print(s.search(nums=[], target=2))
