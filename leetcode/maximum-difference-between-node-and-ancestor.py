# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, min_val, max_val):
        if not root:
            return 0
        min_val = min(root.val, min_val)
        max_val = max(root.val, max_val)
        if not root.left and not root.right:
            return max_val - min_val
        return max(self.dfs(root.left, min_val, max_val), self.dfs(root.right, min_val, max_val))

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, root.val, root.val)