class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        ops = []
        num = 0
        for i in range(1,n+1):
            if i in target:
                ops.append("Push")
                num+=1
            else:
                ops.append("Push")
                ops.append("Pop")
            
            if num == len(target):
                break
        return ops