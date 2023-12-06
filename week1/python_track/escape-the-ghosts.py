class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        for i in ghosts:
            if abs(i[0]-target[0]) + abs(i[1]-target[1]) <= abs(target[0])+abs(target[1]):
                return False
        return True