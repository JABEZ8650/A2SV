class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        summ=0
        count=0
        for i in nums:
            summ+=i
            if summ==0:
                count+=1
        return count