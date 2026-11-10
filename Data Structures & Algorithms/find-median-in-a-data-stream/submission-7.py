class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        heapq.heapify_max(self.left)
        heapq.heapify(self.right)
        

    def addNum(self, num: int) -> None:
        # no elements just insert
        if len(self.left) == 0:
            return heapq.heappush_max(self.left, num)

        # decide to insert in left or right
        if self.left[0] > num:
            heapq.heappush_max(self.left,num)
        else:
            heapq.heappush(self.right, num)

        if abs(len(self.left) - len(self.right)) > 1:
            if len(self.left) > len(self.right):
                ele = heapq.heappop_max(self.left) 
                heapq.heappush(self.right, ele)
            else:
                ele = heapq.heappop(self.right) 
                heapq.heappush_max(self.left, ele)
        

    def findMedian(self) -> float:
        if abs(len(self.left) - len(self.right)) == 0:
            return (self.left[0] + self.right[0])/2
        elif len(self.left) > len(self.right):
            return self.left[0] 
        else:
            return self.right[0]