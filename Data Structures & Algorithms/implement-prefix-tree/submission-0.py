class PrefixTree:

    def __init__(self):
        self.root = {}
        

    def insert(self, word: str) -> None:
        head = self.root
        for char in word:
            if char not in head:
                head[char] = {}

            head = head[char]

        head[None] = None



    def search(self, word: str) -> bool:
        head = self.root
        for char in word:
            if char not in head:
                return False
            head = head[char]
        return None in head
        

    def startsWith(self, prefix: str) -> bool:
        head = self.root
        for char in prefix:
            if char not in head:
                return False
            head = head[char]
        return True
        
        