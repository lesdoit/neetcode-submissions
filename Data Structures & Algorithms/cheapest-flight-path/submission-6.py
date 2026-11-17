class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # modified Dijkstra's where visited node is not ignored 
        # a -(1)->b -(1)->c -(1)-> d
        # |        \__(1)__ \(1)  /(1)        
        # |______(100)______ dest 

        # usually, we check in the condition if d + w < dist[v]. 
        # In addition to this, only for dest, we need to check path_nodes_cnt < k before applying the
        # update
        
        # just doing the check for destination node failed. 
        # trying to incorporate the two suggestions from gemini 
        # 1. don't mark a node as visited once you pop it if the max nodes in path 
        #    has not crossed threshold. Mark as visited only once you pop it and max nodes > k 
        # 2. don't just record dist. Also record dist for each k. So for each node dist[x][k] = 
        #    dist of node x from source with k stops. 

        INF = 1e9
        adj = [[] for _ in range(n)]
        dist = [[INF] * (k + 1) for _ in range(n)]
        visited = [False] * n
        for flight in flights:
            adj[flight[0]].append([flight[1], flight[2]])
        
        # print(f"dist: {dist}")
        pq = [[0, src, 0]]        # dist, node, hops
        while pq: 
            d, u, h = heapq.heappop(pq)
            print(f"d: {d}, u: {u}, h: {h}")
            if h > k: continue
            # visited[u] = True
            #print(f"about to explore neis w prev vals")
            for nei, w in adj[u]:
                # print(f"nei: {nei}, w: {w}, h: {h}")
                if d + w < dist[nei][h]:
                    dist[nei][h] = d + w
                    heapq.heappush(pq, [d+w, nei, h + 1])
        
        print(f"dist: {dist}")
        ans = INF
        for hop in range(k+1):
            ans = min(ans, dist[dst][hop])
        
        return ans if ans != INF else -1

