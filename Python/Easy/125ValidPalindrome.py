from collections import deque 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        
        """
        Brute force solution (using stack)
        
        Time complexity O(2n) -> O(n)
        
        Space complexity O(3n) -> O(n)
        """
        """
        if len(s)<1:
            return True
        
        s_stack = deque()
        
        for char in s:
            
            if char.isalnum():
                s_stack.append(char.lower())
        
        s_list = []
        stack_copy = list(s_stack.copy())
        
        while len(s_stack) > 0:
            s_list.append(s_stack.pop())
        
        return s_list == stack_copy
        """
        
        """
        Efficient solution (using two pointers)
        
        Time complexity O(n)
        Space complexity O(1)
        """
        j = len(s)-1
        i = 0
        while i < j:
            char_two = s[j]
            while not char_two.isalnum() and j>0:
                j-=1
                char_two = s[j]
                
            char = s[i]
            while not char.isalnum() and i<len(s)-1:
                i+=1
                char = s[i]
                
            char = char.lower()
            char_two = char_two.lower()
            j-=1
            i+=1
            if char != char_two and char.isalnum() and char_two.isalnum():
                return False
        
        return True
        