class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)
    
        first = nums[0]
        second = max(first, nums[1])
        max_val = 0
        
        for i in nums[2:]:
            max_val = max(second, first+i)
            first = second
            second = max_val
        return max_val