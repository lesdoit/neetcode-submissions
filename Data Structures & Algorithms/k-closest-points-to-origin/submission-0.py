class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = [(math.sqrt(point[0]**2 + point[1]**2), point[0], point[1]) for point in points]
        heapq.heapify(dists)
        
        ans = []
        while len(ans) < k:
            dist = heapq.heappop(dists)
            ans.append([dist[1], dist[2]])
        
        return ans