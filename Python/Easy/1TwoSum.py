class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        """
        Brute force solution
        
        O(n^2) time
        O(1) space
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
        """         
        """
        Efficient solution
        
        O(n) time
        O(n) space
        """
        targets = {}
        
        for i in range(len(nums)):
            
            targets[target-nums[i]] = i
            
        for i in range(len(nums)):
            val = nums[i]
            if val in targets.keys():
                if targets[val] != i:
                    return [targets[val], i]
        
        """
        Slightly more efficient
        
        Takes only one for loop
        
        O(n) time
        O(n) space
        
        targets = {}
        for index, value in enumerate(nums):
            if targets.get(value) is None:
                targets[target-value] = index
            else:
                return [targets[value], index]
        
        """
            
            
            
        