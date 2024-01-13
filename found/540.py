class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        def bin(l, r):
            print(l, r)
            if l >= r:
                return

            if r == l + 1:
                if nums[l] == nums[r]:
                    return
                if nums[l] != nums[r] and l == 0:
                    return nums[l]
                if nums[l] != nums[r] and r == len(nums) - 1:
                    return nums[r]
                if nums[l] != nums[l - 1]:
                    return nums[l]
                if nums[r] != nums[r + 1]:
                    return nums[r]
                return

            mid = (l + r) // 2
            if (mid - 1 > 0 and nums[mid] != nums[mid - 1]) and (
                mid + 1 < len(nums) and nums[mid] != nums[mid + 1]
            ):
                return nums[mid]
            else:
                a = bin(l, mid)
                if a != None:
                    return a

                b = bin(mid, r)
                if b != None:
                    return b

        if len(nums) == 1:
            return nums[0]
        return bin(0, len(nums) - 1)


s = Solution()
print(s.singleNonDuplicate(nums=[1, 1, 2, 3, 3, 4, 4, 8, 8]))
print(s.singleNonDuplicate(nums=[3, 3, 7, 7, 10, 11, 11]))
print(s.singleNonDuplicate([1]))
print(s.singleNonDuplicate([1, 1, 2]))
print(s.singleNonDuplicate([0, 1, 1]))
