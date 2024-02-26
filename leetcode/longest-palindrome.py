from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        longestPalindrome = len(s)
        oddCharacters = set()
        
        for char in s:
            if char not in oddCharacters:
                oddCharacters.add(char)
            else:
                oddCharacters.remove(char)
        
        if len(oddCharacters):
            longestPalindrome = longestPalindrome - len(oddCharacters) + 1
            return longestPalindrome
        else:
            return longestPalindrome