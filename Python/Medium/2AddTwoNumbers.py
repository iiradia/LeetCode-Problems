# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        first = ""
        head = l1
        while head != None:
            first += str(head.val)
            head = head.next
            print(first)
        
        first = int(first[::-1])
        
        second = ""
        sec = l2
        while sec != None:
            second += str(sec.val)
            sec = sec.next
        second = int(second[::-1])
        
        tot = str(first+second)
        
        ret = list(tot)
        head = None
        for x in ret:
            head = ListNode(x, next=head)
        return head