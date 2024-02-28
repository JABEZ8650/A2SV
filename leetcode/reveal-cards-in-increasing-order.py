class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        N=len(deck)
        sdeck=collections.deque([i for i in range(N)])
        lookup=[None]*N
        t=0
        while len(sdeck)>0:
            top=sdeck.popleft()
            lookup[top]=t
            t+=1
            if len(sdeck)>0:
                top=sdeck.popleft()
                sdeck.append(top)
        ans=[
            deck[lookup[i]] for i in range(N)
        ]
        return ans