class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        visited = set()
        reached = {}
        pacific = set()
        atlantic = set()

        def isValid(row:int, col:int, prev: int):
            return (
                -1 < row < rows and 
                -1 < col < cols and 
                heights[row][col] >= prev and
                (row, col) not in visited
            )


        def visit(row:int, col:int, prev: int, ocean: str):
            if not isValid(row, col, prev):
                return

            if ocean == 'pacific':
                if (row, col) in pacific:
                    return
                pacific.add((row, col))

            if ocean == 'atlantic':
                if (row, col) in atlantic:
                    return
                atlantic.add((row, col))

            visited.add((row,col))
            visit(row + 1, col,     heights[row][col], ocean)
            visit(row - 1, col,     heights[row][col], ocean)
            visit(row,     col + 1, heights[row][col], ocean)
            visit(row,     col - 1, heights[row][col], ocean)
            visited.remove((row,col))

        
        for row in range(rows):
            visit(row, 0,        0, 'pacific')
            visit(row, cols - 1, 0, 'atlantic')


        for col in range(cols):
            visit(0,        col, 0, 'pacific')
            visit(rows - 1, col, 0, 'atlantic')
                

        return list(pacific & atlantic)








            


        