class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ops = 0
        while target > 1:
            while target > 1 and maxDoubles and (target%2 == 0):
                maxDoubles -= 1 
                ops += 1 
                target = target // 2 
            if target > 1 and maxDoubles == 0:
                ops += (target - 1)
                target = 1
                break
            if(target > 1):
                target -= 1 
                ops += 1 
        return ops
            