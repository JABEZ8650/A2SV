class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        r=[]
        if num%3==0:
            r.append((num//3)-1)
            r.append((num//3))
            r.append((num//3)+1)
        return r