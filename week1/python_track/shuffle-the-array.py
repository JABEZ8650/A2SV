class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        #pair values and add them to new list
        new_list=[]
        for i in range(int(len(nums)/2)):
            j=i+n
            new_list.append(nums[i])
            new_list.append(nums[j])
        return new_list