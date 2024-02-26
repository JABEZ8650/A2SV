class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counts={}
        count=0

        for ans in answers:
            if ans==0:
                count+=1
            elif ans not in counts or counts[ans]==0:
                counts[ans]=1
                count += (ans + 1)

            else:
                counts[ans]+=1
                if counts[ans]>ans:
                    counts[ans]=0
        return count