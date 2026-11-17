class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        INF = 1e9
        adj = [[] for _ in range(n)]
        dist = [[INF] * (k + 1) for _ in range(n)]
        visited = [False] * n
        for flight in flights:
            adj[flight[0]].append([flight[1], flight[2]])
        
        pq = [[0, src, 0]]        # dist, node, hops
        while pq: 
            d, u, h = heapq.heappop(pq)
            if h > k: continue
            for nei, w in adj[u]:
                if d + w < dist[nei][h]:
                    dist[nei][h] = d + w
                    heapq.heappush(pq, [d+w, nei, h + 1])
        
        ans = INF
        for hop in range(k+1):
            ans = min(ans, dist[dst][hop])
        
        return ans if ans != INF else -1

