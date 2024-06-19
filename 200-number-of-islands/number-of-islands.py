class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Check if the grid is empty
        if not grid:
            return 0
        
        # Initialize the number of rows and columns
        rows = len(grid)
        cols = len(grid[0])
        
        # Initialize island counter
        island_count = 0
        
        # Define the DFS function
        def dfs(r, c):
            # Check boundaries and if the cell is water
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return
            # Mark the cell as visited by setting it to '0'
            grid[r][c] = '0'
            # Explore the neighbors (up, down, left, right)
            dfs(r - 1, c)  # up
            dfs(r + 1, c)  # down
            dfs(r, c - 1)  # left
            dfs(r, c + 1)  # right
        
        # Iterate through each cell in the grid
        for r in range(rows):
            for c in range(cols):
                # If the cell is land, start a DFS
                if grid[r][c] == '1':
                    dfs(r, c)
                    # Increment the island count
                    island_count += 1
        
        # Return the total number of islands
        return island_count
