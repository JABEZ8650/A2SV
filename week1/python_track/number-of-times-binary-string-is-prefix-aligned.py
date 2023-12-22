class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        ma,count=0,0
        for i in range(len(flips)):
            ma=max(ma,flips[i])
            if i+1>=ma:
                count+=1
        return count