class Solution:

    def validate(self, check:List[str]) -> bool:
        hash = {str(i): 0 for i in range(1,10)};

        for x in check:
            if not x == ".":
                hash[x] += 1

        for key, value in hash.items():
            if value > 1:
                return False

        return True 

        

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check = []

        ''' rows '''
        for row in board:
            check.append(row)

        ''' cols ''' 
        for col in range(0,9):
            check.append([board[row][col] for row in range(0,9)])
            
        ''' group ''' 

        for row_loop in range(0,9,3):
            for col_loop in range(0,9,3):
                group =[
                    board[row][col]
                    for row in range(row_loop, row_loop + 3)
                    for col in range(col_loop, col_loop + 3)
                ]
                check.append(group)

        print(check)

        for group in check:
            if not self.validate(group):
                return False;
        
        return True

        