# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        side_start = None
        node_start = None

        def dfs(node, side=None):
            if node.val == start:
                nonlocal side_start, node_start
                side_start = side
                node_start = node

            if node.left:
                dfs(node.left, side or "left")
            if node.right:
                dfs(node.right, side or "right")

        def max_depth(node):
            if not node:
                return 0, 0, 0
            l_depth = 1 + max_depth(node.left)[0]
            r_depth = 1 + max_depth(node.right)[0]
            return max(l_depth, r_depth), l_depth, r_depth

        