# Bottom up approach
class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n == 0):
            return 0
        elif(n ==1 or n==2):
            return 1
        n = n + 1 
        bottom = [None] * n
        bottom[0] = 0
        bottom[1] = 1
        bottom[2] = 1
        for i in range(3,n):
            bottom[i] = bottom[i-1]+bottom[i-2]+bottom[i-3]
        return bottom[n -1]