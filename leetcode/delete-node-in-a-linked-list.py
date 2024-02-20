# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        # locate victim node
        victim_node = node.next
        
        # overwrite node's value by victim node's value
        node.val = victim_node.val
        
        # break the linkage of victim node
        node.next = victim_node.next
        
        # release victim node
        del victim_node
        
        return