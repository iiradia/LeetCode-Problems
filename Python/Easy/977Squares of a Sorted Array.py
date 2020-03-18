class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        #element-wise for loop
        return sorted([i**2 for i in A])
    
        #index-wise for loop
        return sorted([A[i]**2 for i in range(len(A))])