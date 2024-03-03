# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(node,arr):
            if node is None:
                return None
            
            inorder(node.left,arr)
            arr.append(node)
            inorder(node.right,arr)
        
        def construct(arr):
            if not arr:
                return None
            
            mid = len(arr)//2
            
            node = TreeNode(arr[mid].val)
            node.left = construct(arr[:mid])
            node.right = construct(arr[mid+1:])
            
            return node
            
        arr = []
        inorder(root,arr)
        
        return construct(arr)