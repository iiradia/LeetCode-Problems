class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        """
        Efficient solution
            - use rule about summing range of numbers from 1 to n
            - subtract by sum of list
        
        Time complexity O(n)
        Space complexity O(1)
        """
        total_sum = (len(nums)*(len(nums)+1))/2
        
        return int(total_sum - sum(nums))
    