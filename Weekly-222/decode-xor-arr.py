class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        arr = [first]
        i = 0
        for item in encoded:
            arr.append(arr[i] ^ item)
            i += 1
        return arr