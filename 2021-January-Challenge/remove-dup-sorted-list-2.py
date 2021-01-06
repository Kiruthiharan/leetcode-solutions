# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        dummy = ListNode(-1)
        dummy.next = head
        fast, slow = head, dummy
        while fast:
            while fast.next and fast.val == fast.next.val:
                fast = fast.next
            if slow.next == fast:
                slow, fast = slow.next, fast.next
            else:
                slow.next = fast.next
                fast = slow.next
                
        return dummy.next