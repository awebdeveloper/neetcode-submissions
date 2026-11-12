class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.result = []
        self.n = n*2

        def dfs(array:List[str]):
            if (
                len(array) > self.n or 
                array.count('(') < array.count(')') or
                array.count('(') > self.n/2
            ):
                return

            if len(array) == self.n and  array.count('(') == array.count(')'):
                return  self.result.append(array)
                

            # ( branch
            dfs(array + [')'])

            # ) branch
            dfs(array + ['('])

        dfs(['('])

        result = ["".join(x) for x in self.result]
        return result

