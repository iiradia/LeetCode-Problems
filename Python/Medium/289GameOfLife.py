from copy import deepcopy
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        # step 1 -> make helper method called live_neighbors that finds all live neighbors
        # step 2 -> make second helper called find_neighbors that returns array of all neighbors
        # step 3 -> iterate through every cell and change based on protocol
        
        def find_neighbors(b, row, col):
            """
            Takes in a cell and identifies all of its neighbors.
            """
            neighbors = []
            neigh_r = [row+1,row-1,row]
            neigh_c = [col+1,col-1,col]
            board_len = len(b)
            
            for r in neigh_r:
                for c in neigh_c:
                    # make sure it is not this cell
                    if r!=row or c!= col:
                        if r>=0 and c>=0 and r<board_len and c<len(b[r]):
                            neighbors.append(b[r][c])
        
            return neighbors
                
        
        def live_neighbors(b, row, col):
            """
            Use find_neighbors to find number of neighbors
            to a cell that are live.
            """
            neighbors = find_neighbors(b, row, col)
            
            # return neighbors that are live
            return neighbors.count(1)
        
        b2 = deepcopy(board)
        for row in range(len(b2)):
        
            for col in range(len(b2[row])):
                
                live_neighbor_count = live_neighbors(b2,row,col)
                cell = b2[row][col]
                is_live = cell == 1
                
                if is_live:
                    if live_neighbor_count < 2 or live_neighbor_count > 3:
                        board[row][col] = 0
                else:
                    if live_neighbor_count == 3:
                        board[row][col] = 1
        
        return board