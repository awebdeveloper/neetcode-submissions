class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.found = False
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])
        self.word = word
        self.processed = set()
        self.word_len = len(word)

        def dfs(row:int, col:int, current_word: str):
            if ((row,col) in self.processed or # dont go back
                row < 0 or row >= self.rows or # dont go out of bounds
                col < 0 or col >= self.cols or  # dont go out of bounds
                len(current_word) > self.word_len or # more than the word
                self.found == True # result alreday found ignore
            ):
                return

            # add current sq to word
            current_word += self.board[row][col]
            if current_word  == self.word:
                self.found = True


            self.processed.add((row,col))
            dfs(row-1, col,   current_word)
            dfs(row+1, col,   current_word)
            dfs(row,   col+1, current_word)
            dfs(row,   col-1, current_word)
            self.processed.remove((row,col))

        for row in range(0,self.rows): 
            for col in range(0,self.cols):
                if self.found:
                    return self.found
                dfs(row, col, "")

        return self.found


