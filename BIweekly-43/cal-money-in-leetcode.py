class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        mon = 1
        day = 1
        result = 0
        while(n != 0):
            if (day == 8):
                mon += 1
                day = 1
            result += mon + day -1
            day +=1
            n -= 1  
        return result
        