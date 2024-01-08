class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums)
        while r - l > 0:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid
            elif nums[mid] < target:
                l = mid + 1
        return -1


s = Solution()
print(s.search(nums=[-1, 0, 3, 5, 9, 12], target=9))
print(s.search(nums=[-1, 0, 3, 5, 9, 12], target=2))
print(s.search(nums=[-1], target=2))
print(s.search(nums=[-1], target=-1))
print(s.search(nums=[-1, 2], target=-1))
print(s.search(nums=[-1, 2], target=2))
print(s.search(nums=[], target=2))
