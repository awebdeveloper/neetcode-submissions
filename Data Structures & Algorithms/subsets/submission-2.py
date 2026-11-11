class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result  = []
        def dfs(i, subset):

            # Exclude
            for j in range(i, len(nums)):
                self.result.append(subset + [nums[j]])
                dfs(j+1, subset + [nums[j]])

        dfs(0, [])
        return self.result + [[]]