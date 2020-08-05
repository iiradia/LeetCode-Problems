class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        def check_diagonal_validity(arr, row, col):

            while row<len(arr)-1 and col<len(arr[row])-1:
                element_value = arr[row][col]
                row+=1
                col+=1 
                if element_value != arr[row][col]:
                    return False

            return True

        if len(matrix) < 1:
            return True

        for index in range(len(matrix[0])):

            if not check_diagonal_validity(matrix, 0, index):
                return False

        for row in range(1,len(matrix)):

            if not check_diagonal_validity(matrix, row, 0):
                return False

        return True
    
        