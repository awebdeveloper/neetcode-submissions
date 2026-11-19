class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def isValidCell(row:int, col: int) -> bool:
            return (
                -1 < row < rows and 
                -1 < col < cols and 
                grid[row][col] != -1 and 
                grid[row][col] != 0 and 
                (row,col) not in visited
            )

        def find(row:int, col: int, distance: int = 0):
            if not isValidCell(row, col):
                return
            
            queue = collections.deque()
            queue.append((row, col, distance))

            while queue:
                row, col, distance = queue.popleft()

                if not isValidCell(row, col):
                    continue

                # alreday shorter path exists
                if grid[row][col] <= distance:
                    continue

                grid[row][col] = distance
            
                visited.add((row, col))
                queue.append((row - 1, col,     distance + 1))
                queue.append((row + 1, col,     distance + 1))
                queue.append((row,     col - 1, distance + 1))
                queue.append((row,     col + 1, distance + 1))
                visited.remove((row, col))


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    find(row - 1, col,     1)
                    find(row + 1, col,     1)
                    find(row,     col - 1, 1)
                    find(row,     col + 1, 1)

        

            

            


 