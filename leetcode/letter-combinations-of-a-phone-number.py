class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []
        
        phone_dict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        result = []
        
        def dfs(idx, temp):
            if idx == len(digits):
                result.append(''.join(temp))
                return
            
            for letter in phone_dict[digits[idx]]:
                dfs(idx + 1, temp + [letter])
            
        dfs(0, [])
        return result