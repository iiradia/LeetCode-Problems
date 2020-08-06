import re
import string
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        for i in range(len(word)):
            for char in range(len(word)): 
                n = list(word)
                n[char] = '.'
                try:
                    n[char+i] = '.'
                except: pass
                self.words[''.join(n)] = 1
        
        self.words[word] = 1

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        print(self.words.get(word))
        return self.words.get(word) is not None


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)