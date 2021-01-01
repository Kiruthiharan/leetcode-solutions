class Solution(object):
    def canFormArray(self, arr, pieces):
        """
        :type arr: List[int]
        :type pieces: List[List[int]]
        :rtype: bool
        """
        dict = {}

        for i, items in enumerate(pieces):
            for j, item in enumerate(items):
                dict[item] = [i,j]


        i = 0
        while (i < len(arr)):
            if(arr[i] in dict.keys()):
                j = dict[arr[i]]
            else:
                return(False)
            x = 0
            while(x < len(pieces[j[0]])):
                if(arr[i] == pieces[j[0]][x]):
                    i += 1
                    x += 1
                    continue
                return(False)
            
        return(True)