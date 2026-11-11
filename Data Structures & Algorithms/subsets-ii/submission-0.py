class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.result = [[]]
        nums.sort()

        def dfs(i: int, sublist: List[int]):
            if i >= len(nums):
                return


            for j in range(i, len(nums)):
                if i == j or nums[j] != nums[j-1]:
                    self.result.append(sublist + [nums[j]])
                    dfs(j + 1, sublist + [nums[j]])

        
        dfs(0,[])
        return self.result




