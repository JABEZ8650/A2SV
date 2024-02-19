class Solution:
    def corpFlightBookings(self, bookings, n: int):
        ans=[0]*(n+1)

        for i,j,k in bookings:
            ans[i-1]+=k
            ans[j]-=k

        ans.pop()

        for i in range(1,len(ans)):
            ans[i]+=ans[i-1]

        return ans