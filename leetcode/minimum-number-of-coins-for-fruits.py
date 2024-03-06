class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [inf for _ in range(n+1)]
        dp[-1] = 0

        for i in range(n-1,-1,-1):
            for j in range(i+1, min(i+i+3, n+1)):
                dp[i] = min(dp[i], dp[j] + prices[i])

        return dp[0]