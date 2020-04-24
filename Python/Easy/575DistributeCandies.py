class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        unique = len(set(candies))
        half_len = len(candies) / 2
        
        if unique <= half_len:
            return unique
        
        else:
            return half_len
               
        