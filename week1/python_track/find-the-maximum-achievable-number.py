class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        x=0
        for i in range(t):
            num+=1
            x+=1
        return num+x