class Solution(object):
    def processQueries(self, queries, m):
        """
        :type queries: List[int]
        :type m: int
        :rtype: List[int]
        """
        p = list(range(1, m+1))
        result = []
        for i in range(len(queries)):
            x = p.index(queries[i])
            result.append(x)
            p.insert(0, p.pop(x))
     
        return result
    