class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = 0
        a = []
        for i in range(len(nums)):
            if nums[i] == 1:
                c += 1
            else:
                a.append(c)
                c = 0
        a.append(c)
        return max(a)