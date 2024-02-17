class Solution:
    def removeDuplicates(self, s: str) -> str:
        idx =0
        while(idx+1<len(s)):
            if(s[idx]==s[idx+1]):
                s= s[:idx]+s[idx+2:]
                if idx > 0:
                    idx -= 1
            else:
                idx += 1
        return s