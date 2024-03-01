class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        run = True
        a = 0
        while run:
            if 3**a >= n:
                ans = False
                run = False
            if 3**a == n:
                ans = True
                run = False
            a += 1
        return ans