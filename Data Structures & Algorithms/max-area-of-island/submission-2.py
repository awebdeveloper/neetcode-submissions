class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        maxArea = 0


        def isValidIslandCell(cell: tuple[int, int]) -> bool:
            row, col = cell

            return (
                -1 < row < rows and 
                -1 < col < cols and 
                cell not in visited and
                grid[row][col] == 1
            )

        def getArea(position: tuple[int, int]) -> int:
            queue = collections.deque()
            queue.append(position)
            visited.add(position)
            area = 1

            while queue:
                ele = queue.popleft()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                for dirs in directions:
                    cell = (ele[0] + dirs[0], ele[1] + dirs[1])
                    if isValidIslandCell(cell):
                        area += 1
                        queue.append(cell)
                        visited.add(cell)
            return area

        for row in range(rows):
            for col in range(cols):

                if isValidIslandCell((row, col)):
                    area = getArea((row, col))
                    maxArea = max(area, maxArea)

        
        return maxArea
        
        
        