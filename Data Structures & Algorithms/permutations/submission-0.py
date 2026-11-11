class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []

        def dfs(i: int, sublist: List[int]):
            if i >= len(nums):
                return self.result.append(sublist)

            for ele in nums:
                if ele not in sublist:
                    dfs(i+1, sublist + [ele])

        dfs(0,[]*len(nums))
        return self.result

