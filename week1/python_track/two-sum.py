class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j and nums[i]+nums[j]==target and len(ans)!=2:
                    ans.append(i)
                    ans.append(j)
        return ans