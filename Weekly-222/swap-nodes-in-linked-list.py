# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        length = 0
        ptr = head
        while(ptr != None):
            length += 1
            ptr = ptr.next
        first = k
        last = length - k + 1
        fNode = None
        lNode = None
        count = 0
        ptr = head
        while(ptr != None):
            count += 1
            if(count == first):
                fNode = ptr
            if(count == last):
                lNode = ptr
            ptr = ptr.next
        fNode.val , lNode.val = lNode.val, fNode.val
        return head