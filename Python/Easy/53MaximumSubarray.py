class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        """
        1. Go through each element in the list
        2. Go through every other element and a. identify its part of the contiguous subarray
        b. if that sum is bigger than the max
        3. return the max
        """
        """
        if (len(nums) == 1):
            return nums[0]
        count = 0
        for i in range(len(nums)):
            
            current_sum = nums[i]
            if (current_sum > max_sum):
                max_sum = current_sum
            count = 0
            
            for j in range(len(nums)):
                
                if (abs(i - j) <= (count+1) and i != j):
                    
                    current_sum += nums[j]
                    if (current_sum > max_sum):
                        max_sum = current_sum
                    count+=1
        return max_sum
        """
    
        """
        Use dynamic programming.
        Keep track of the current max at each element and the overall maximum based
        on the options at each element.
        
        O(n) time complexity
        O(1) space complexity
        """
        curr_sum = nums[0]
        max_sum =  nums[0]
        
        for i in range(1, len(nums)):
            
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)
                
        return max_sum