class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        num_soldiers = 0 
        for n in range(len(rating)):
            for i in range(n, len(rating)):
                for j in range(i, len(rating)):
                    
                    a = rating[n]
                    b = rating[i]
                    c = rating[j]
                    valid = (a < b and b < c) or (c < b and b < a)
                    valid_index = (n < i and i < j)
                    
                    if (a!= b and b != c and a != c and valid and valid_index):
                        num_soldiers += 1
                        
        return num_soldiers
                    
            
        