class Solution:
    def lastSubstring(self, s: str) -> str:
        
        max_substring = ""
        
        for i in range(len(s)):
            max_substring = max(max_substring, s[i:])
        
        return max_substring