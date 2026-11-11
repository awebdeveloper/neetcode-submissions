class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        self.result = []
        nums.sort()

        def dfs(i:int, sublist:List[int], total:int):
            # on match store result
            if total == target and sublist not in self.result:
                return self.result.append(sublist)

            
            # end loop when elements are over or sum exceeds target
            if i >= len(nums) or total > target:
                return

            for j in range(i,  len(nums)):
                #skip if current and prev is same but include nums[i] irespective
                if j==i or nums[j] != nums[j-1]:
                    dfs(j+1, sublist + [nums[j]], total + nums[j])

           
        dfs(0,[],0)

        return self.result

[1]


