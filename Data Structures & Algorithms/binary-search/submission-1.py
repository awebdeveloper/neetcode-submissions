class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1 
        
        while start <= end:
            mid = int((start + end)/2)
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
        
        return -1
