class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7
        cumm_odds, cumm_even, res =0, 0, 0
        
        for a in arr:
            if a%2:
                cumm_odds, cumm_even = cumm_even+1, cumm_odds
            else:
                cumm_even+=1
                
            res+=cumm_odds
            
        return res%mod