class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        one = curr_max = 0
        res = 0
        for i in flips:
            one += 1
            curr_max = max(curr_max , i)
            
            if one == curr_max:
                res += 1
        return res