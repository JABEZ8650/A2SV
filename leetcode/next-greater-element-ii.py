class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        curr = nums[0]
        stack = [nums[0]]
        for i in range(len(nums)):
            if nums[i] > curr:
                curr = nums[i]
                stack.append(nums[i])
        stack = stack[::-1]
        k = len(nums)
        ans = [-1]*(k)
        for i in range(k-1,-1,-1):
            while stack and nums[i] >= stack[-1]:
                stack.pop()
            if stack:
                ans[i] = stack[-1]
            stack.append(nums[i])
        return ans


        