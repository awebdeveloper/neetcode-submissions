class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)

        if k > len(nums):
            k = len(nums)

        i = 0
        while nums and i < k-1:
            heapq.heappop_max(nums)
            i += 1

        return nums[0]
