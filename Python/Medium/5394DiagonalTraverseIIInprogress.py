class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        
        [[1,2,3],[4,5,6],[7,8,9]]
[[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
[[1,2,3],[4],[5,6,7],[8],[9,10,11]]
[[1,2,3,4,5,6]]
[[6],[8],[6,1,6,16]] --> this is currently failing
        """
        if len(nums) == 1:
            return nums[0]
        num_diagonals = len(nums) + max([len(i) for i in nums]) - 1
        print(num_diagonals)
        num_r = range(1, num_diagonals+1)
        #median_diagonal = int(num_r[len(num_r)/2])
        median_diagonal = len(nums)
        print(median_diagonal)
        current_diagonal = 1
        first_half = [[] for _ in range(median_diagonal)]
        second_half = [[] for _ in range(median_diagonal-1)]
        
        while current_diagonal <= median_diagonal:
            print("Currently on diagonal", current_diagonal)
            for row in range(current_diagonal-1, -1, -1):
                for col in range(0, current_diagonal):
                    if row+col == current_diagonal-1:
                        #print((row, col))
                        #print(first_half)
                        first_half[current_diagonal-1].append([row, col])
            current_diagonal += 1
            
        
        while current_diagonal <= num_diagonals:
            print ("Currently on diagonal", current_diagonal)
            dist_away = current_diagonal - median_diagonal
            flipped_indices = first_half[median_diagonal - dist_away - 1]
            flipped_indices = flipped_indices[::-1]
            for diagonals in flipped_indices:
                second_half[current_diagonal-median_diagonal-1].append([diagonals[1]+dist_away, diagonals[0]+dist_away])
            
            current_diagonal += 1
        
        idxs=[]
        print("FIRST")
        print(first_half)
        print("SECOND")
        print(second_half)
        first_half.extend(second_half)
        for a in first_half:
            for b in a:
                try: 
                    idxs.append(nums[b[0]][b[1]])
                except: pass
        

        return idxs
                        
        