class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # solution1
        nums = nums + list(range(0,len(nums)+1))
        ans = 0
        for i in nums:
            ans ^= i
        return ans
