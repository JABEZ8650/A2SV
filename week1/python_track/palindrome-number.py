class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=list(str(x))
        z=y[::-1]  
        for i in range(len(y)):
            if y[i]!=z[i]:
                return False
        return True