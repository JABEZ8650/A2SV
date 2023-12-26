class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        pair=dict(zip(heights,names))
        na=[]
        for key, value in sorted(pair.items(),reverse=True):
            na.append(pair[key])
        return na
