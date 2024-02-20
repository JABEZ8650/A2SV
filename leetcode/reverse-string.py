class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(s, start, end):
            if start>=end:
                return
            s[start],s[end]=s[end],s[start]

            reverse(s, start+1, end-1)

        return reverse(s, 0, len(s)-1)