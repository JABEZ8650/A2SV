class Solution:
    # def dp(self,i,buy,prices,fee,n,dct):
    #     if i==n:
    #         return 0
    #     if (i,buy) in dct:
    #         return dct[(i,buy)]
    #     if buy:
    #         x=max(self.dp(i+1,buy,prices,fee,n,dct),self.dp(i+1,0,prices,fee,n,dct)-prices[i])
    #     else:
    #         x=max(self.dp(i+1,buy,prices,fee,n,dct),self.dp(i+1,1,prices,fee,n,dct)+prices[i]-fee)
    #     dct[(i,buy)]=x
    #     return x

    def maxProfit(self, prices: List[int], fee: int) -> int:
        n=len(prices)
        # dp=[[0]*2 for _ in range(n+1)]
        ahd=[0]*2
        for i in range(n-1,-1,-1):
            curr=[0]*2
            for buy in range(2):
                if buy:
                    curr[buy]=max(ahd[buy],ahd[0]-prices[i])
                else:
                    curr[buy]=max(ahd[buy],ahd[1]+prices[i]-fee)
            ahd=curr
        return ahd[1]

        # return self.dp(0,1,prices,fee,n,{})