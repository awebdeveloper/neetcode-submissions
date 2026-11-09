class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closestPoint = []
        heapq.heapify_max(closestPoint)

        for i  in range(len(points)):
            distance = math.sqrt(points[i][0] ** 2 + points[i][1] ** 2)
            heapq.heappush_max(closestPoint, (distance,i,points[i]))

            if len(closestPoint) > k:
                heapq.heappop_max(closestPoint)


        return [point for _,_, point in closestPoint]



        