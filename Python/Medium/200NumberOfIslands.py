class Solution(object):
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(grid, i, j):
            """
            Helper method for depth first search.
            """
            # error checking (off the grid)
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
                return 0 
            if grid[i][j] == '0':
                return 0
            
            # sink island
            grid[i][j] = '0'

            # visit up, down, left, right
            dfs(grid, i + 1, j)
            dfs(grid, i - 1, j)
            dfs(grid, i, j + 1)
            dfs(grid, i, j - 1)

            return 1
    
        if grid==None or len(grid)==0:
           return 0
        
        num_islands = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    
                    num_islands += dfs(grid, i, j)
        
        return num_islands