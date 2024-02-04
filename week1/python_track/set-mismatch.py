class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = []
        set_nums = set()

        for num in nums:
            if num in set_nums:
                ans.append(num)
            else:
                set_nums.add(num)


        sum_all_unique_nums = sum(set(set_nums))
        sum_original_set = N*(N+1)/2
        missing_number = int(sum_original_set - sum_all_unique_nums)
        ans.append(missing_number)

        return ans