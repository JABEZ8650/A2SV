class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        lst=[]
        ma=0
        for num in points:
            lst.append(num[0])
        lst.sort()
        for j in range(len(lst)-1):
            ma=max(ma, lst[j+1]-lst[j])
        return ma