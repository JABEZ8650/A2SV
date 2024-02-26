class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key= lambda x: x[0])
        start=points[0][0]
        end=points[0][1]
        shoot=0

        for i,j in points:
            if start<=i<=end or start<=j<=end:
                start=max(start,i)
                end=min(end,j)
            else:
                shoot+=1
                start=i
                end=j

        return shoot+1

       