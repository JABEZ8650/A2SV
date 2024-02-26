class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        mistake = 0
        open = 0
        for i in s:
            if i == "(":
                open += 1
            elif i == ")":
                if open > 0:
                    open -= 1
                else:
                    mistake += 1

        return open + mistake