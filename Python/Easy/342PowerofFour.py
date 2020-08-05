class Solution:
    def isPowerOfFour(self, num: int) -> bool:
         
         if num == 1:
            return True
        
         while num > 4:
                num /= 4
        
         return num == 4