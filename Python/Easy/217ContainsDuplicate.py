class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Efficient solution
        O(n) time
        O(n) space
        """
        seen = {}
        for num in nums:
            if num in seen:
                return True
            seen[num] = 1
        return False