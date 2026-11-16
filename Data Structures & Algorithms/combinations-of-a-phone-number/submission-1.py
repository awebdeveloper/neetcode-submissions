class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.result = []
        self.hash  = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }

        def dfs(i: int, till_now: str):
            if i >= len(digits):
                return self.result.append(till_now)

            for alphabet in self.hash[digits[i]]:
                dfs(i + 1, till_now + alphabet)

        if digits:
            dfs(0,'')

        return self.result


'''
d
e
f

dg
'''