class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
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
                len(current_word) > self.word_len # length more than the word
            ):
                return

            # add current sq to word
            current_word += self.board[row][col]
            if current_word  == self.word:
                return True


            self.processed.add((row,col))
            result = (
                dfs(row-1, col,   current_word) or
                dfs(row+1, col,   current_word) or
                dfs(row,   col+1, current_word) or
                dfs(row,   col-1, current_word)
            )
            self.processed.remove((row,col))
            return result

        for row in range(0,self.rows): 
            for col in range(0,self.cols):
                if (word[0] == board[row][col]):
                    if dfs(row, col, "") == True:
                        return True

        return False


