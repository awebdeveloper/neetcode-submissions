class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeroCount = nums.count(0);

        if zeroCount > 1:
            return [0] * len(nums);

        for x in nums:
            product *= x or 1

        result = []
        for x in nums:
            numerator = product
            demominator = x
            if x != 0 and zeroCount == 1:
                numerator = 0
            elif x == 0:
                demominator = 1
            result.append(numerator//demominator)

        return result
        