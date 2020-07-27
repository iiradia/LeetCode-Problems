class Solution:
    def frequencySort(self, s: str) -> str:
        
        unique = {char:s.count(char) for char in set(s)}
        unique= {char:unique[char] for char in sorted(unique,key=unique.get,reverse=True)}
        strs = []
        
        for char in unique:
            strs.append(char*unique[char])
        
        return ''.join(strs)
        