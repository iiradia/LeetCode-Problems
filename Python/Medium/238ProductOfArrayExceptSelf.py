class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        """
        Brute force
        
        O(N^2) time complexity
        O(1) space complexity (excluding output array)
        
        output = []
        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i != j:
                    prod *= nums[j]
            output.append(prod)
        
        return output
        """
        """
        Optimized solution. Using left array and right counter.
        
        O(N) time complexity
        O(1) extra space complexity
        """
        output = [1] * len(nums)
        for i in range(1,len(nums)):
            output[i] = output[i-1]*nums[i-1]
        
        right = 1
        for j in reversed(range(len(nums))):
            output[j] *= right
            right *= nums[j]
        
        return output
            
        