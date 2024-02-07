# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nums = []
        curr = head
        while curr:
            nums.append(curr.val)
            curr = curr.next
        
        N = len(nums)
        res = 0
        for i in range(N // 2):
            res = max(res, nums[i] + nums[N - i - 1])
        return res