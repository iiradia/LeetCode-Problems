class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        # if even number of letters in each, they are the same
        map_1 = {}
        map_2 = {}
        
        for idx in range(len(s)):
            
            if map_1.get(s[idx]) is None:
                map_1[s[idx]] = 1
            else:
                map_1[s[idx]] +=1
                
            if map_2.get(t[idx]) is None:
                map_2[t[idx]] = 1
            else:
                map_2[t[idx]] +=1
            
        return map_1 == map_2
        