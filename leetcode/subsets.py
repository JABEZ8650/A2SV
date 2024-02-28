class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i, path, length):
            if len(path) == length:
                ans.append(path[:])
                return
            
            for j in range(i, N):
                path.append(nums[j])
                backtrack(j + 1, path, length)
                path.pop()
        
        ans = []
        N = len(nums)
        
        for l in range(N + 1):
            backtrack(0, [], l)
        return ans