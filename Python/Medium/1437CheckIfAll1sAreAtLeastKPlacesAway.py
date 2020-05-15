class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        one_idx = 0
        count = 0
        current_idx = 0
        idx = 0
        for i in nums:
            if i == 1:
                one_idx = current_idx
                current_idx = idx
                dist = current_idx - one_idx - 1
                if dist < k and count != 0:
                    return False
                count+=1
            idx+=1
        return True
            