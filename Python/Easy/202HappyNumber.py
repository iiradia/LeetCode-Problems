class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def sum_square(n):
            return sum([int(i)**2 for i in str(n)])
        
        tgt = 0
        dup = set()
        while True:
            tgt = sum_square(n)
            n = tgt
            if tgt == 1:
                return True
            if n in dup:
                return False
            
            dup.add(n)
        