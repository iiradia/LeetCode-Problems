class Solution:
    def printVertically(self, s: str) -> List[str]:
        
        words = s.split(' ')
        output = ["" for i in range(len(max(words, key = len)))] 
        
        for i in range(len(words)):
            for char in range(len(output)):
                if char >= len(words[i]):
                    output[char] += ' '
                else:
                    output[char] += words[i][char]
        
        # strip from output
        for i in range(len(output)):
            output[i] = output[i].rstrip()
        
        return output
                
        
        """
        TO BE OR NOT TO BE
        
        T O 
        B E 
        O R 
        N O T
        T O 
        B E
        """