# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n
        mid = n / 2
        curr = n
        
        while (left < right):
            if isBadVersion(mid):
                curr = mid
                right = mid-1
                mid = (right + left) / 2
            else:
                left = mid+1
                mid = (right + left) / 2
        
        if (isBadVersion(left)):
            return left
        return curr