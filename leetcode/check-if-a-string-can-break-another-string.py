class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        lst1, lst2 = sorted(s1), sorted(s2)
        return (all(a >= b for a, b in zip(lst1, lst2)) or
                all(a <= b for a, b in zip(lst1, lst2)))