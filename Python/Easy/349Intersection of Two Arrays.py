#Python

"""
Leetcode Problem #349. Intersection of Two Arrays
@author Ishaan Radia
@author Harshal Suthar
"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
      
      #Solution with checking if array is unique
      inter = []
      
      for i in nums1:
        	if i in nums2 and i not in inter:
                inter.append(i)
      return inter