# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        prev = None
        next_node = None
        
        while curr is not None:
            
            #change values
            next_node = curr.next
            curr.next = prev
            
            #set pointers to traverse
            prev = curr
            curr = next_node
           
        head = prev
        return head