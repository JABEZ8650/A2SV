class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        temp=[]
        
        def backtrack(m):

            if k== len(temp):
                ans.append(temp[:])
                return
            
            for num in range(m, n+1):
                temp.append(num)
                backtrack(num+1)
                temp.pop()

        backtrack(1)
        return ans