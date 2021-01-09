#TLE SAD
class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        self.res = 0
        self.a = []
        def dfs(sub):
            if(len(sub) < 2):
                return 0
            length = len(sub)
            i = 0
            temp = 0 
            while(i < length - 1):
                p1 = sub[i]
                p2 = sub[i+1]
                if( sub[i:i+2] == "ab" ):
                    temp = max(dfs(sub[:i] + sub[i+2:]) + x, temp)
                elif( sub[i:i+2] == "ba" ):
                    temp = max(dfs(sub[:i] + sub[i+2:]) + y, temp)
                i += 1
            return temp

        return dfs(s)
            
        
