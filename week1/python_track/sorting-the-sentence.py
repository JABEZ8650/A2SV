class Solution:
    def sortSentence(self, s: str) -> str:
        words=s.split()
        arr=[0]*len(words)
        for word in words:
            idx = int(word[-1])-1
            arr[idx] = word[:-1]
        return ' '.join(arr)