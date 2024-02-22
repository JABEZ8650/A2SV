class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        target = sum(nums) % p # targetted remainder 
        ans = inf
        seen = {(prefix := 0): -1}
        for i, x in enumerate(nums): 
            seen[(prefix := (prefix+x)%p)] = i # update seen before check 
            if (prefix-target) % p in seen: 
                ans = min(ans, i - seen[(prefix-target) % p])
        return ans if ans < len(nums) else -1 # not allowed to remove whole array 