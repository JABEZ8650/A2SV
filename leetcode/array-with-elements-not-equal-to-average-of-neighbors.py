class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        i = 0
        j = len(nums) - 1
        res = []
        while i <= j:
            if i == j:
                res.append(nums[i])
                break
            res.append(nums[i])
            res.append(nums[j])
            i += 1
            j -= 1
        return res