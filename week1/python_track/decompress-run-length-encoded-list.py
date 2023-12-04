class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        y=[]
        for i in range(len(nums)-1):
            if i%2==0:
                y+=[nums[i+1]]*nums[i]
        return y