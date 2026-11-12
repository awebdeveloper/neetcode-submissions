class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.found = False
        self.board = board
        self.v_size = len(board)
        self.h_size = len(board[0])
        self.word = word
        self.processed = set() 

        def dfs(v:int, h:int, current_word: str):
            if ((v,h) in self.processed or # dont go back
                v < 0 or v >= self.v_size or # dont go out of bounds
                h < 0 or h >= self.h_size or  # dont go out of bounds
                self.found == True # result alreday found ignore
            ):
                return

            # add current sq to word
            current_word += self.board[v][h]
            if current_word  == self.word:
                self.found = True


            self.processed.add((v,h))
            dfs(v-1, h,   current_word)
            dfs(v+1, h,   current_word)
            dfs(v,   h+1, current_word)
            dfs(v,   h-1, current_word)
            self.processed.remove((v,h))

        for i in range(0,self.v_size): 
            for j in range(0,self.h_size):
                if self.found:
                    return self.found
                dfs(i, j, "")

        return self.found


