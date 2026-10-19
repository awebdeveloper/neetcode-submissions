class Solution:

    def isValid(self, s: str) -> bool:
        array = []
        hash = {
            '(':')',
            '{':'}',
            '[':']',
        }

        for char in s:  
            if char in hash:
                array.append(char)
            else:
                if len(array) > 0 and hash.get(array[-1],0) == char:
                    array.pop()
                else:
                    return False

        return True if len(array) == 0 else False 