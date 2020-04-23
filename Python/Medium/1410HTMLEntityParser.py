class Solution(object):
    def entityParser(self, text):
        """
        :type text: str
        :rtype: str
        """
       
        text = text.replace("&quot;", '"')
        text = text.replace("&apos;", "'")
        text = text.replace("&amp;", "&")
        text = text.replace("&gt;", ">")
        text = text.replace("&lt;", "<")
        text = text.replace("&frasl;", "/")
        return text
                    
        