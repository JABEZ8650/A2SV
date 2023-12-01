class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strg=""
        m=sorted(strs)
        ini=m[0]
        las=m[-1]
        for i in range(min(len(ini),len(las))):
            if ini[i]!=las[i]:
                return strg
            strg+=ini[i]
        return strg