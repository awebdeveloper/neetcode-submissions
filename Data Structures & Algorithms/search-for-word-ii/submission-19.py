class Solution:
    def __init__(self) -> None:
         self.tree = {}  

    def buildTree(self, word: str) -> None:
        root = self.tree

        for char in word:
            if  char not in root:
                root[char] = {}
            root = root[char]

        root['#'] = word
        

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.result = []
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])
        self.biggest = 0
        self.words = set(words)

        for x in words:
            self.buildTree(x)
            self.biggest = max(self.biggest, len(x))


        def dfs(paths: Set[tuple[int, int]], current: tuple[int, int], tree: dict):
            row, col = current

            if (
                not self.words or # no more words
                len(paths) >= self.biggest or # bigger than biggest word
                row < 0 or row >= self.rows or # outside rows
                col < 0 or col >= self.cols or # outside cols
                current in paths # already traversed
            ):
                return

            char = board[row][col]
            if not char in tree: # is it a partial or full match
                return
            
            if '#' in tree[char] and tree[char]['#'] in self.words:
                self.words.remove(tree[char]['#'])
                self.result.append(tree[char]['#'])

                
            paths.add((row,col))
            dfs(paths, (row + 1, col),     tree[char])
            dfs(paths, (row - 1, col),     tree[char]) 
            dfs(paths, (row,     col + 1), tree[char]) 
            dfs(paths, (row,     col - 1), tree[char])
            paths.remove((row,col))


        for row in range(self.rows):
            for col in range(self.cols):
                dfs(set(), (row, col), self.tree)

        return self.result
