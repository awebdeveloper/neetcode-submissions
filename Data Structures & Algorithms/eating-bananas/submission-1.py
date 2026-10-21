class Solution:
    def remaining(self, piles: List[int], hours: int, speed: int):
        remaining = hours
        for i in range(len(piles)):
            remaining -= math.ceil(piles[i] / speed)

        return remaining

    def minEatingSpeed(self, piles: List[int], hours: int) -> int:
        left, right = 1, max(piles)
        res = right

        while left <= right:
            mid = (left+right) // 2 
            answer = self.remaining(piles=piles, hours=hours, speed=mid)
            if answer >= 0:
                right = mid - 1
                res = min(res, mid)
            elif answer < 0:
                left = mid + 1

        return res


    
