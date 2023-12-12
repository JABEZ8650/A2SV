class Solution:
    def isHappy(self, n: int) -> bool:
        while n!=1 and (len(str(n))!=1 or n==7):
            sum=0
            n=str(n)
            for i in n:
                sum+=int(i)**2
            n=sum
        if n==1:
            return True
        else:
            return False