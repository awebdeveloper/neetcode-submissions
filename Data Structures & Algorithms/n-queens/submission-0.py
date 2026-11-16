class Solution:
    def isFail(self, till_now: List[str]) -> bool:
        cols = len(till_now[-1])
        rows = len(till_now)
        prevQ = till_now[-1].index('Q')
        fwdDiagonal, revDiagonal = prevQ, prevQ

        for row in range(rows - 2, -1, -1):
            #verticle match
            if till_now[row][prevQ] == 'Q':
                return True

            # fwd diagonal match
            fwdDiagonal += 1
            if fwdDiagonal < cols and till_now[row][fwdDiagonal] == 'Q':
                return True
            
            # rev diagonal match
            revDiagonal -= 1
            if revDiagonal >= 0 and till_now[row][revDiagonal] == 'Q':
                return True

        return False



    def solveNQueens(self, n: int) -> List[List[str]]:
        self.result = []
        self.row = '.' * n
        self.n = n

        def dfs(i: int, till_now: List[str]):
            if i > 1 and self.isFail(till_now):
                return

            if i >= self.n:
                return self.result.append(till_now)

            for col in range(0, self.n):
                row = self.row[0:col] + 'Q' + self.row[col+1:]
                dfs(i + 1, till_now + [row])

       
        dfs(0,[])
        self.isFail(["..Q.","Q...",".Q.."])

        return self.result