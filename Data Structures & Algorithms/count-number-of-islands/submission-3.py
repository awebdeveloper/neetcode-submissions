class Solution:
    
    
    def isNewIslandCell(self, row: int, col: int):
        return (
            0 <= row < self.rows and
            0 <= col < self.cols and 
            self.grid[row][col] == '1' and
            (row,col) not in self.visited
        )

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        self.rows = len(grid)
        self.cols = len(grid[0])
        self.visited = set()
        self.grid = grid
        islands = 0

        def dfs(row: int, col: int):
            if self.isNewIslandCell(row, col):
                self.visited.add((row, col))
                return (
                    dfs(row + 1, col) or
                    dfs(row - 1, col) or
                    dfs(row, col + 1) or
                    dfs(row, col - 1)
                )
                

        for row in range(self.rows):
            for col in range(self.cols):
                if self.isNewIslandCell(row, col):
                    dfs(row, col)
                    islands += 1

        return islands