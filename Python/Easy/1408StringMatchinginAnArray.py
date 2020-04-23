class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        matched = []
        for word in words:
            for word2 in words:
                if word != word2 and word in word2:
                    matched.append(word)

        return set(matched)