class Solution:
    def getMax(self, nums: list[int], start:int, end:int) -> Tuple(int, int):
        maxN = (0, float('-inf'))
        for i in range(start, end + 1):
            if nums[i] >= maxN[1]:
                maxN = (i,nums[i])
        return maxN
    
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxInWindow = self.getMax(nums, 0, k-1)

        result = [maxInWindow[1]]

        for start in range(1, len(nums)-k+1):
            end = start + k - 1;

            if maxInWindow[0] < start:
                maxInWindow = self.getMax(nums, start, end)
            elif maxInWindow[1] <= nums[end]:
                maxInWindow = (end, nums[end])

            result.append(maxInWindow[1])

        return result