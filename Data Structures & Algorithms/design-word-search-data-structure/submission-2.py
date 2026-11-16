class WordDictionary:

    def __init__(self):
        self.root = {}
        

    def addWord(self, word: str) -> None:
        head = self.root
        for char in word:
            if char not in head:
                head[char] = {}
            head = head[char]
        head[None] = None
        

    def search(self, word: str) -> bool:
        def ds(part: str, head: dict):
            if part and not head:
                return False

            for i in range(len(part)):
                if part[i] == '.':
                    for key, childTree in head.items():
                        if key is None:
                            continue

                        if ds(part[i+1:], childTree):
                            return True
                    return False
                elif part[i] in head:
                    return ds(part[i+1:], head[part[i]])
                else:
                    return False

            return None in head

        return ds(word, self.root)


        
