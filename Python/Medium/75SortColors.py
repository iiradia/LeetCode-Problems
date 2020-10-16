class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        
        """
        [2 0 2 1 1 0]
         ^
         since 2, swap to 'end'
         
        [0 0 2 1 1 0]
           ^ 
        0, swap to 'start'
        """
        
        start = 0
        end = len(nums) - 1
        idx = 0
        
        while idx <= end:
            
            if nums[idx] == 2:
                nums[idx] = nums[end]
                nums[end] = 2
                end -= 1
            
            elif nums[idx] == 0:
                nums[idx] = nums[start]
                nums[start] = 0
                start += 1
                idx += 1
            
            else:
                idx += 1