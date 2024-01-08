class Solution:
    def binsearch(self, a, key, l, r):
        if r >= l:
            mid = (l + r) // 2
            if a[mid] == key:
                return mid
            elif a[mid] < key:
                return self.binsearch(a, key, mid + 1, r)
            else:
                return self.binsearch(a, key, l, mid - 1)
        else:
            return -1

    def search(self, nums: list[int], target: int) -> int:
        return self.binsearch(nums, target, 0, len(nums) - 1)


s = Solution()
print(s.search(nums=[-1, 0, 3, 5, 9, 12], target=9))
print(s.search(nums=[-1, 0, 3, 5, 9, 12], target=22))
print(s.search(nums=[-1, 0, 3, 5, 9, 12], target=2))
print(s.search(nums=[-1], target=2))
print(s.search(nums=[-1], target=-1))
print(s.search(nums=[-1, 2], target=-1))
print(s.search(nums=[-1, 2], target=2))
print(s.search(nums=[], target=2))
