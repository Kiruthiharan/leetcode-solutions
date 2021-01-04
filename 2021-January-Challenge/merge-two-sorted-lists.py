# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# should search a more optimized solution 
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if(l1 == None and l2 == None):
            return l1
        result = None
        ans = result
        while(l1 != None and l2 != None):
            if(l1.val <= l2.val):
                val = l1.val
                l1 = l1.next
            else:
                val = l2.val
                l2 = l2.next
            if(ans == None):
                result = ListNode(val)
                ans = result
            else:
                result.next = ListNode(val)
                result = result.next
        if(l1 != None):
            if(ans == None):
                result = l1
                ans = result
            else:
                result.next = l1
        if(l2 != None):
            if(ans == None):
                result = l2
                ans = result
            else:
                result.next = l2
            
        return(ans)