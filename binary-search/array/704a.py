def bin_search(l, r, nums, target):
    # print(l, r)
    if r - l <= 0:
        return -1
    mid = l + (r - l) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        return bin_search(l, mid, nums, target)
    elif nums[mid] < target:
        return bin_search(mid + 1, r, nums, target)


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        return bin_search(0, len(nums), nums, target)


s = Solution()
print(s.search(nums=[-1, 0, 3, 5, 9, 12], target=9))
print(s.search(nums=[-1, 0, 3, 5, 9, 12], target=2))
print(s.search(nums=[-1], target=2))
print(s.search(nums=[-1], target=-1))
print(s.search(nums=[-1, 2], target=-1))
print(s.search(nums=[-1, 2], target=2))


mids = []


def explore(l, r, nums, target):
    print(l, r)
    if r - l <= 0:
        return -1
    mid = l + (r - l) // 2
    mids.append(mid)
    explore(l, mid, nums, target)
    explore(mid + 1, r, nums, target)


# explore(0, 9, [1, 2, 3], 2)
# print(sorted(mids))
