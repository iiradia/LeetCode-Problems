class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return([i for i in A if i%2==0]+[i for i in A if i%2!=0])

    
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        
        output = []
        for i in range(len(A)):
            if A[i] % 2 == 0:
                output.append(A[i])
            
        for i in range(len(A)):
            if A[i] % 2 != 0:
                output.append(A[i])
            
        return output
        