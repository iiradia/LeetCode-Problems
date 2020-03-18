import itertools
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        code = set()
        for c in s:
            if c not in code:
                code.add(c)
            else:
                code.remove(c)
        return len(s) - len(code) + 1 if len(code) > 0 else len(s)