class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def dfs(k):
            if k == 1:
                return 0
            parent_ind = (k + 1) // 2
            parent = dfs(parent_ind)
            if parent == 0:
                if k % 2:
                    return 0
                else: 
                    return 1
            if parent == 1:
                if k % 2:
                    return 1
                else:
                    return 0
        return dfs(k)