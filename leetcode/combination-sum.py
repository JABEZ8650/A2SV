class Solution:
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        N = len(candidates)
        
        def dfs(i, temp, remaining_nums):
            if remaining_nums == 0:
                result.append(list(temp))
                return
            
            if remaining_nums < 0 or i == N:
                return 
            
            dfs(i, temp + [candidates[i]], remaining_nums - candidates[i])
            dfs(i + 1, temp, remaining_nums)
        
        dfs(0, [], target)
        return result