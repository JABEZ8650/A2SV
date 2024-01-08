class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        fi=0
        while l<len(nums):
            if nums[l]!=0:
                nums[l],nums[fi]=nums[fi],nums[l]
                fi+=1
            l+=1