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

        def bfs(position: tuple[int, int]):
            queue = collections.deque()
            queue.append(position)
            self.visited.add(position)

            while queue:
                ele = queue.popleft()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                for r, c in directions:
                    row = ele[0] + r
                    col = ele[1] + c

                    if self.isNewIslandCell(row, col):
                        queue.append((row, col))
                        self.visited.add((row, col))
                


        for row in range(self.rows):
            for col in range(self.cols):
                if self.isNewIslandCell(row, col):
                    bfs((row, col))
                    islands += 1

        return islands