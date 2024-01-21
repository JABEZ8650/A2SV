class Solution:
    def numSubarraysWithSum(self, nums: List[int], g: int) -> int:
        d={}
        d[0]=1
        pre=0
        ans=0
        for i in range(len(nums)):
            pre+=nums[i]
            
            t=pre-g
            if t in d:
                ans+=d[t]
            if pre in d:
                d[pre]+=1
            else:
                d[pre]=1
            
        return ans