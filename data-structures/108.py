# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]):
        mid = len(nums) // 2
        l_nums = nums[: mid - 1]
        r_nums = nums[mid + 1 :]
        left = self.sortedArrayToBST(l_nums) if l_nums else None
        right = self.sortedArrayToBST(r_nums) if r_nums else None
        return TreeNode(nums[mid], left, right)
