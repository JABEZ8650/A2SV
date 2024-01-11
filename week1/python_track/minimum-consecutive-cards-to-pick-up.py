class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        if len(set(cards))==len(cards):
            return -1
        dic={}   
        ma=1000000
        for i in range (len(cards)):
            if cards[i] not in dic:
                dic[cards[i]]=i
            else:
                if ma>(i-(dic[cards[i]])):
                    ma=(i-dic[cards[i]])
                dic[cards[i]]=i
        return ma+1
