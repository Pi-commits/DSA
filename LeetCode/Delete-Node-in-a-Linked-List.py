# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# First Solution
# class Solution:
#     def deleteNode(self, node):
#         """
#         :type node: ListNode
#         :rtype: void Do not return anything, modify node in-place instead.
#         """
        
#         while node:
#             if node.next:
#                 node.val = node.next.val
#                 if not node.next.next:
#                     node.next = None
#                     break
#                 node = node.next
        
    
# Second Solution
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        node.val = node.next.val
        node.next = node.next.next
        
        return 
        
