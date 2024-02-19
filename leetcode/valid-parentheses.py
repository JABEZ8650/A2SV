class Solution:
    def isValid(self, s: str) -> bool:
        lst=[]
        all={"}":"{",")":"(","]":"["}
        for i in s:
            if i in all.values():
                lst.append(i)
            elif lst and all[i]==lst[-1]:
                lst.pop()
            else:
                return False
        return lst==[]