class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        #creat a hash map that track the number of apperance of elements
        tracker={}
        for num in nums:
            if num not in tracker:
                tracker[num]=1
            else:
                tracker[num]+=1

        #checking the elements apperance
        output=[]
        for key, value in tracker.items():
            if value>(len(nums)/3):
                output.append(key)
        
        return output