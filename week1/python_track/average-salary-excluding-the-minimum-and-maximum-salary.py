class Solution:
    def average(self, salary: List[int]) -> float:
        x=min(salary)
        y=max(salary)
        z=x+y
        summ=sum(salary)-z
        return summ/(len(salary)-2)