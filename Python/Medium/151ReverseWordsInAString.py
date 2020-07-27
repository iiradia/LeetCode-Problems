class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        st = reversed(s.strip().split(" "))
        new = ""
        
        for i in st:
            if len(i)>0:
                new+=i.strip(" ")
                new+=" "
        return new.strip()