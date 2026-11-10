class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result  = []

        self.sublist = []
        def dfs(i):
            if i >= len(nums):
                return self.result.append([*self.sublist])

            self.sublist.append(nums[i])
            dfs(i+1)

            self.sublist.pop()
            dfs(i+1)

        dfs(0)   
        return self.result


'''
[1]
'''


            