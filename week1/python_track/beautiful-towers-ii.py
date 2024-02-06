class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        left = [0] * n
        right = [0] * n
        
        ## For every height, find the closest peak to its left which has a height less than it
        stk = []
        for i in range(n):
            while stk and maxHeights[stk[-1]] >= maxHeights[i]: stk.pop()
            left[i] = i - (stk[-1] if stk else -1)
            stk.append(i)
            
        ## Similarly, for every height, find the closest peak to its right which has a height less than it
        stk = []
        for i in range(n-1, -1, -1):
            while stk and maxHeights[stk[-1]] >= maxHeights[i]: stk.pop()
            right[i] = (stk[-1] if stk else n) - i
            stk.append(i)
           
        ## For a given position, find its contribution towards its left such that it maintains the mountain property
        @cache
        def getLeftMax(i):
            if i < 0: return 0
            return (left[i] * maxHeights[i]) + getLeftMax(i - left[i])
        
        ## For a given position, find its contribution towards its right such that it maintains the mountain property
        @cache
        def getRightMax(i):
            if i >= n: return 0
            return (right[i] * maxHeights[i]) + getRightMax(i + right[i])
            
        ## Finally, consider every height as the peak of the mountain and calculate the sum
        maxSum = 0
        for i in range(n):
            curMax = maxHeights[i]
            leftMax = getLeftMax(i)
            rightMax = getRightMax(i)
            maxSum = max(maxSum, leftMax + rightMax - curMax) ## curMax gets counted twice
        return maxSum
            