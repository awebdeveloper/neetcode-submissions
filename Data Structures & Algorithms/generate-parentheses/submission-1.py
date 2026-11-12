class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.result = []
        self.n = n*2

        def dfs(array:List[str]):
            if (
                len(array) > self.n or # gone above
                array.count('(') < array.count(')') or # imbalance more )
                array.count('(') > self.n/2 #imbalance ( than half
            ):
                return

            # valid entry
            if len(array) == self.n and  array.count('(') == array.count(')'):
                return  self.result.append(array)
                

            # ( branch
            dfs(array + [')'])

            # ) branch
            dfs(array + ['('])

        dfs(['('])

        result = ["".join(x) for x in self.result]
        return result

