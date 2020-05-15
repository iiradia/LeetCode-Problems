class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return [i for i in list(set(nums)) if nums.count(i) == 1][0]
        