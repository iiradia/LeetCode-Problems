class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        lucky = []
        for i in arr:
            
            if arr.count(i) == i:
                lucky.append(i)
                
        if len(lucky) > 0:
            return max(lucky)
        
        else:
            return -1