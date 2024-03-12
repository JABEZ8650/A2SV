class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start,subset):
            res.append(subset)
            for i in range(start,len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                backtrack(i+1,subset+[nums[i]])
        res = []
        nums.sort()
        backtrack(0,[])
        return res