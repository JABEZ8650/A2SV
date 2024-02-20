class Solution:
    def fib(self, n: int) -> int:
        if n==1:
            return 1
        if n==0:
            return 0
        
        first= self.fib(n-1)
        second= self.fib(n-2)

        return first + second