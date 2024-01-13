# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # dfs
        def max_depth(node):
            if not node:
                return 0
            l_depth = 1 + max_depth(node.left)
            r_depth = 1 + max_depth(node.right)
            return max(l_depth, r_depth)


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # bfs
        queue = [root]
        depth = 0
        while queue:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            depth += 1
