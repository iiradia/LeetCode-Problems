class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        
        [[1,2,3],[4,5,6],[7,8,9]]
[[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
[[1,2,3],[4],[5,6,7],[8],[9,10,11]]
[[1,2,3,4,5,6]]
[[6],[8],[6,1,6,16]]
        """
        length = len(nums)
        cols = max([len(i) for i in nums])
        idxs = [[] for _ in range(len(nums)+cols-1)]

        
        for row in range(length-1, -1, -1):
            for col in range(len(nums[row])):
                try:
                    idxs[row+col].append(nums[row][col])
                except: pass
            
        return [j for i in idxs for j in i]
                        