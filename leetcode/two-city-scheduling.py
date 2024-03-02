class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        order= sorted(costs, key = lambda x: x[0]-x[1])
        
        middle= int(len(costs)/2)
        
        min_cost=0
        for i in range(len(order)):
            if i<middle:
                min_cost+=order[i][0]
            else:
                min_cost+=order[i][1]

        return min_cost