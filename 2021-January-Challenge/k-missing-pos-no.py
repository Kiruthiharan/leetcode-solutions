class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        i = 1
        x = 0
        pos = 0
        while(x < len(arr)):
            if(arr[x] != i):
                if(pos == k - 1):
                    return i
                pos += 1
                i += 1
            else:
                x += 1
                i += 1
        return(i + (k - pos) - 1)