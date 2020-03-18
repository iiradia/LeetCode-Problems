class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        product = 1
        summ = 0
        
        for i in range(len(str(n))):
            
            x = int(str(n)[i])
            product *= x
            summ +=x
            
        return product - summ
        
        