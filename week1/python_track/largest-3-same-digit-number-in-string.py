class Solution:
    def largestGoodInteger(self, num: str) -> str:
        w=""
        k=""
        z=[]
        num=list(num)
        for i in range(len(num)-2):
            if num[i]==num[i+1] and num[i+1]==num[i+2] and num[i]==num[i+2]:
                w+=num[i]
                w+=num[i+1]
                w+=num[i+2]
            if len(w)==3:
                z.append(w)
                w=""
        if len(z)==0:
            return k
        else:
            win=max(z)
            return str(win)