class Solution:
    def reverseWords(self, s: str) -> str:
        t=s.strip(" ")
        l=t.split(" ")
        p=[]
        for i in l:
            if(i!=""):
                p.append(i)
        m=""
        for i in p[::-1]:
            m=m+i+" "
        return m.rstrip()