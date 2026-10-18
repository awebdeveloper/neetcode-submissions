class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        product = 1
        for i in range(0, len(nums)-1):
            product *= nums[i]
            result[i+1] *= product

        product = 1
        for i in range(len(nums)-1, 0, -1):
            product *= nums[i]
            result[i-1] *= product
        

        return result
        