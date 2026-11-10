class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result  = []
        def dfs(i, subset):
            if i >= len(nums):
                self.result.append(subset)
                return

            # Exclude
            dfs(i+1, subset)

            # Include
            dfs(i+1, subset + [nums[i]])

        dfs(0, [])
        return self.result