class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s=''
        mi=min(len(word1),len(word2))
        for i in range(mi):
            s+=word1[i]
            s+=word2[i]
        if mi<len(word1):
            s+=word1[i+1:len(word1)+1]
        elif mi<len(word2):
            s+=word2[i+1:len(word2)+1]
        return s