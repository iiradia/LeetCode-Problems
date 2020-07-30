class Solution:
    def isValid(self, s: str) -> bool:
        
        close_map = {"(":")", "[":"]", "{":"}"}
        
        seen = []
        
        for char in s:
            
            if close_map.get(char) is None:
                if len(seen) < 1:
                    return False
                if close_map[seen[-1]] != char:
                    return False
                else:
                    seen.pop()
            else:
                seen.append(char)
          
        if len(seen) > 0:
            return False
        return True