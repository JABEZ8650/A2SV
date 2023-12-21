class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=''.join(map(str, digits))
        nums=int(num)+1
        ans=[int(i) for i in str(nums)]
        return ans