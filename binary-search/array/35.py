class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid

        print(l, mid, r)
        return l


s = Solution()
# s.searchInsert(nums=[1, 3, 5, 6], target=-1)
# s.searchInsert(nums=[1, 3, 5, 6], target=1)
# s.searchInsert(nums=[1, 3, 5, 6], target=2)
# s.searchInsert(nums=[1, 3, 5, 6], target=3)
# s.searchInsert(nums=[1, 3, 5, 6], target=5)
# s.searchInsert(nums=[1, 3, 5, 6], target=7)


def search(nums, target):
    l = 0
    r = len(nums)
    while l < r:
        mid = (l + r) // 2
        print(l, mid, r)
        if nums[mid] >= target:
            r = mid
        else:
            l = mid + 1
    print(l, mid, r)


search([1, 2, 4, 4, 5, 5, 5, 7], 8)
# search([1, 2, 4, 5, 5, 5, 7], 6)
# search([1, 2, 4, 5, 5, 5, 7], 7)
# search([1, 2, 4, 5, 5, 5, 7], 8)
