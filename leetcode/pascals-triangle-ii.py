class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]
        
        val=self.getRow(rowIndex-1)

        arr=[]
        for i in range(len(val)-1):
            arr.append(val[i]+val[i+1])
        
        return [1]+arr+[1]