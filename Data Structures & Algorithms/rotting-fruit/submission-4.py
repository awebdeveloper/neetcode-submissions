class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visitedHash = {} 

        def isValidCell(row:int, col: int) -> bool:
            isValid = (
                -1 < row < rows and 
                -1 < col < cols and 
                grid[row][col] == 1
            )

            return isValid

        def rot(row:int, col: int):
            if not isValidCell(row, col):
                return
            
            queue = collections.deque()
            queue.append((row, col, 1))

            while queue:
                row, col, timeElapsed = queue.popleft()

                if not isValidCell(row, col):
                    continue

                # alreday shorter path exists
                if (row, col) in visitedHash and visitedHash[(row, col)] <= timeElapsed:
                    continue

                visitedHash[(row, col)] = timeElapsed
                queue.append((row - 1, col,     timeElapsed + 1))
                queue.append((row + 1, col,     timeElapsed + 1))
                queue.append((row,     col - 1, timeElapsed + 1))
                queue.append((row,     col + 1, timeElapsed + 1))


        for row in range(rows):
            for col in range(cols):

                if grid[row][col] == 0:
                    visitedHash[(row, col)] = 0
                    
                if grid[row][col] == 2:
                    visitedHash[(row, col)] = 0
                    rot(row - 1, col,   )
                    rot(row + 1, col,   )
                    rot(row,     col - 1)
                    rot(row,     col + 1)

        print(visitedHash)
        cellsToVisited = rows * cols - len(visitedHash)  

        if cellsToVisited > 0:
            return -1

        return max(visitedHash.values())

        


        

            

            


 