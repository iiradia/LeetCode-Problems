class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        """
        Brute force solution

        O(n) time
        O(n) space
        """
        seen = {}
        twice = []
        
        for num in nums:
            if seen.get(num) is not None:
                twice.append(num)
            seen[num] = 1
        
            
        return twice

        """
        Efficient solution

        O(n) time
        O(1) space
        """
