class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 1000000007
        n = len(arr)
        nextSmaller = [i for i in range(n)]
        stack = []
        for i in range(n - 1, -1, -1):
            while len(stack) > 0 and arr[stack[-1]] > arr[i]:
                stack.pop()
            if len(stack) > 0:
                nextSmaller[i] = stack[-1]
            stack.append(i)
        dp = [inf for _ in range(n)]
        for i in range(n - 1, -1, -1):
            if i == nextSmaller[i]:
                dp[i] = (arr[i] * (n - i)) % mod
            else:
                dp[i] = (((nextSmaller[i] - i) * arr[i]) + dp[nextSmaller[i]]) % mod
        return sum(dp) % mod
