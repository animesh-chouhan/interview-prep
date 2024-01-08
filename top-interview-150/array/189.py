class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            nums.insert(0, nums.pop())


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        net_rot = k % len(nums)
        for _ in range(net_rot):
            nums.insert(0, nums.pop())


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        net_rot = k % len_nums
        nums = nums[len_nums - net_rot :] + nums[: len_nums - net_rot]

        print(nums)


s = Solution()
s.rotate([1, 2, 3, 4, 5, 6, 7], 3)
