# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head == None or head.next == None):
            return head
        ptr = head
        flag = 0
        prev = None
        while(ptr!=None and ptr.next!=None):
            temp = ptr.next
            ptr.next = temp.next
            temp.next = ptr
            if(prev!=None):
                prev.next = temp
            prev = ptr
            ptr = ptr.next
            if(flag==0):
                head = temp
                flag =1
        return head
            