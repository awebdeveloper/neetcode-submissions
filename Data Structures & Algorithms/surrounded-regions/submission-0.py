class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        visited = set()
        connected = set()

        def isValid(row:int, col:int) -> bool:
            return(
                -1 < row < rows and 
                -1 < col < cols and 
                (row, col) not in visited and
                (row, col) not in connected and
                board[row][col] == 'O'
            )

        def visit(row:int, col:int):
            if not isValid(row, col):
                return

            connected.add((row, col))

            visited.add((row, col))
            visit(row + 1, col)
            visit(row - 1, col)
            visit(row,     col + 1)
            visit(row,     col - 1)
            visited.remove((row, col))


        # left and Right
        for row in range(rows):
            visit(row, 0)
            visit(row, cols -1)
        
        # top and bottom
        for col in range(cols):
            visit(0,    col)
            visit(rows - 1, col)

        # mark not connected as X
        for row in range(rows):
            for col in range(cols):
                if (row, col) not in connected:
                    board[row][col] = 'X'


