from collections import defaultdict
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        index = defaultdict(list)
        for i, num in enumerate(nums):
            index[num].append(i)
        n = len(nums)
        res = [0]*len(nums)
        for num in index:
            prev = index[num][0]
            n = len(index[num])
            left = right = 0
            for j in index[num]:
                right += j - prev
            for j, i in enumerate(index[num]):
                left += j*(i-prev)
                right -= (n - j)*(i-prev)
                res[i] = left + right
                prev = i
        return res