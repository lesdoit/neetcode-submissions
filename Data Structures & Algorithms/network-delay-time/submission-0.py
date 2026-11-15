import collections, heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # single source shortest path with no negative edge weights (implies no negative cycle)
        # Dijkstra's is applicable 
        
        visited = [False] * (n+1)
        dist = [1e9] * (n+1)
        adj = [[] for _ in range(n+1)]
        pq = []
        
        def create_graph():
            for time in times:
                adj[time[0]].append((time[1], time[2]))
        
        def dijkstra(k):
            dist[k] = 0
            heapq.heappush(pq, (0, k))
            while pq:
                d, u = heapq.heappop(pq)
                
                if visited[u]: continue
                visited[u] = True
                
                for nei, w in adj[u]:
                    if d + w < dist[nei]:
                        dist[nei] = d + w
                        heapq.heappush(pq, (d+w, nei))
            
            # print(f"dist: {dist}")
        
        create_graph()
        dijkstra(k)

        ans = -1
        for node in range(1, n+1):
            if not visited[node]: return -1
            ans = max(ans, dist[node])
        return ans 

