class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        left = 0
        window = {}

        for right in range(n):
            if nums[right] not in window:
                window[nums[right]] = 0
            window[nums[right]] += 1

            while max(window) - min(window) > 2:
                window[nums[left]] -= 1
                if window[nums[left]] == 0:
                    del window[nums[left]]
                left += 1

            count += right - left + 1

        return count
        