class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        all_lowercase = True
        num_capital = 0
        only_first = True
        for i in range(len(word)):
            if word[i] == word[i].upper():
                all_lowercase = False
                num_capital += 1
                if i != 0:
                    only_first = False
        return all_lowercase or only_first or num_capital == len(word)
                
            