class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution 1 - almost naive
# Speed - 93, Mem - 18
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ptr1 = l1
        ptr2 = l2
        bal = 0
        root = None
        ptr = root
        x = 0
        y = 0
        while(ptr1 != None or ptr2!= None):
            if(ptr1 != None):
                x = ptr1.val
                ptr1 = ptr1.next
            else:
                x = 0
            if(ptr2 != None):
                y = ptr2.val
                ptr2 = ptr2.next
            else:
                y = 0
            temp = x + y + bal
            ans = temp % 10
            bal = int(temp / 10)
            if(root == None):
                root=ListNode(ans)
                ptr = root
            else:
                ptr.next = ListNode(ans)
                ptr = ptr.next
        if(bal != 0):
            ptr.next = ListNode(bal)
        return (root)
