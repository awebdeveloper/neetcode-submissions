class Solution:
    def partition(self, s: str) -> List[List[str]]:

        self.string = list(s)

        self.result  = []

        def isPali(string: str) -> bool:

            print(string)
            end = len(string)
            for i in range(end // 2):
                if string[i] != string[end - i-1]:
                    return False

            return True


        def  dfs(i: int, till_now:List[str]):
            if i >= len(self.string):
                if isPali(till_now[-1]):
                    self.result.append(till_now)
                return  

            last = till_now.pop()

            if isPali(last):
                dfs(i+1, till_now + [last, s[i]])
            dfs(i+1, till_now + [last + s[i]])

        dfs(1, [s[0]])
        return self.result

        

        