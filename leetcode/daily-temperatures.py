class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        lst = []
        ans=[0]*len(temperatures)

        for i, value in enumerate(temperatures):
            while lst and temperatures[lst[-1]] < value:
                index = lst.pop()
                ans[index] = i - index
            lst.append(i)
        
        return ans