class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five=[]
        ten=[]
        
        for bill in bills:
            if bill==5:
                five.append(bill)
            if bill == 10:
                if five:
                    five.pop()
                    ten.append(bill)
                else:
                    return False
            if bill == 20:
                if five and ten:
                    five.pop()
                    ten.pop()
                elif len(five)>=3:
                    five.pop()
                    five.pop()
                    five.pop()
                else:
                    return False

        return True