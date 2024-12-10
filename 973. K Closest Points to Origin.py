from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = self.distance(points)

        # Put everything in max heap
        heap = []
        for i in range(len(points)):
            heapq.heappush(heap,  (-distances[i], points[i]))
            if len(heap) > k:
                heapq.heappop(heap)

        # get k closest points
        closest = []
        while heap:
            _, point = heapq.heappop(heap)
            closest.append(point)

        return closest

    def distance(self, points: List[List[int]]) -> List[int]:
        distance = []
        for point in points:
            dist = math.sqrt((point[0]**2) + (point[1]**2))
            distance.append(dist)
        
        return distance