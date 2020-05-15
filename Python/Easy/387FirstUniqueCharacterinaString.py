class Solution(object):
    def firstUniqChar(self, s):
        """
        --> Faster than 97.33& of Python submissions.
        :type s: str
        :rtype: int
        """
        s_set = list(set(s))
        try:
            return min([s.index(i) for i in s_set if s.count(i) == 1])
        except:
            return -1
        