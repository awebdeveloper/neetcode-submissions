class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for out in range(0, len(nums)-1):
            for inner in range(out+1, len(nums)):
                if nums[inner] + nums[out] == target:
                    return [out, inner]

        