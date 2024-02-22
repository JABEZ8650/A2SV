class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 1
        forwardSums = [0] * n
        backSums = [0] * n

        forwardSums[0] = nums[0]
        forwardSums[1] = nums[1]
        for i in range(2, n):
            forwardSums[i] = forwardSums[i - 2] + nums[i]

        backSums[-1] = nums[-1]
        backSums[-2] = nums[-2]
        for i in range(n - 3, -1, -1):
            backSums[i] = backSums[i + 2] + nums[i]

        def isFair(idx: int):
            sum1 = (forwardSums[idx - 2] if idx - 2 >= 0 else 0) + (backSums[idx + 1] if idx + 1 < n else 0)
            sum2 = (forwardSums[idx - 1] if idx - 1 >= 0 else 0) + (backSums[idx + 2] if idx + 2 < n else 0)
            return sum1 == sum2

        output = 0
        for i in range(len(nums)):
            output += int(isFair(i))
        return output