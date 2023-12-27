class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ord=sorted(nums)
        my_dict={}
        lst=[]
        for i,v in enumerate(ord):
            if v not in my_dict.keys():
                my_dict[v]=i                
        for i in nums:
            lst.append(my_dict[i])
        return lst