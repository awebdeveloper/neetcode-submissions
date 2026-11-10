class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.result = []

        def dfs(i:int, sublist:List[int]):
            # end loop when elements are over or sum exceeds target
            if i >= len(nums) or sum(sublist) > target:
                return

            # on match store result
            if sum(sublist) == target and sublist not in self.result:
                return self.result.append(sublist)

            # same number once more
            dfs(i, sublist + [nums[i]])

            # exclude current
            dfs(i+1, sublist)

        dfs(0,[])
        return self.result


           
