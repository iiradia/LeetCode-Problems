class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        less_ct = []
        for focal_num in nums:
            less=0
            for other in nums:
                
                if focal_num != other and other < focal_num:
                    less += 1
            
            less_ct.append(less)
            
        return less_ct
        