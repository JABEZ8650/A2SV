class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums)%k!=0:
            return False
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        while d:
            a=min(d)
            b=d[a]
            for i in range(a,k+a):
                if i not in d:
                    return False
                else:
                    d[i]-=b
                    if d[i]==0:
                        del d[i]
        return True