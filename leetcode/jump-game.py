class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return True

        dp = [False] * n
        dp[0] = True
        for i, num in enumerate(nums):
            for j in range(i + 1, min(n, i + num + 1)):
                if dp[j - 1]:
                    dp[j] = True
            
            if dp[-1]:
                return True
        
        return dp[-1]
