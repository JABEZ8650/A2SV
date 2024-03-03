    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.size = len(arr)
        self.tree = [0] * (4*self.size)
        self.build_tree(0,0,self.size-1)
    
    def build_tree(self, i, L, R):
        if L == R:
            self.tree[i] = (self.arr[L], L)
            return self.tree[i]
        M = L + (R-L)//2
        self.tree[i] = max(
            self.build_tree(2*i + 1, L, M),
            self.build_tree(2*i + 2, M+1, R),
            key=lambda x: x[0])
        return self.tree[i]

    def query(self, i, L, R, l, r):
        if r < L or R < l: 
            return (-maxsize,-1)
        if L >= l and R <= r:
            return self.tree[i]
        M = L + (R-L)//2
        return max(
            self.query(2*i + 1, L, M, l, r),
            self.query(2*i + 2, M+1, R, l, r),
            key=lambda x: x[0])

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        tree = SegmentTree(nums)

        def dfs(l=0, r=len(nums)-1):
            if l == r:
                return TreeNode(nums[l])
            ma = tree.query(0,0,tree.size-1,l,r)
            node = TreeNode(ma[0])
            node.left = dfs(l,ma[1]-1) if ma[1]-1 >= l else None
            node.right = dfs(ma[1]+1, r) if ma[1]+1 <= r else None
            return node

        return dfs()