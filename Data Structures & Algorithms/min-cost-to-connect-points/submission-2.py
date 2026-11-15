class DSU:
    def __init__(self, n):
        self.rank = [1] * n
        self.parent = [i for i in range(n)]
    
    def find(self, x):
        # find parent w path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        # union by size/rank 
        xp = self.find(x)
        yp = self.find(y)
        
        if xp == yp: return False

        if self.rank[xp] < self.rank[yp]:
            xp, yp = yp, xp
        
        self.parent[yp] = self.parent[xp]

        if self.rank[xp] == self.rank[yp]:
            self.rank[xp] += 1
        
        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = [[] for _ in range(n)]

        pq = []
        
        def manhattan(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        def create_graph():
            for i in range(n):
                for j in range(i+1, n):
                    adj[i].append([j, manhattan(points[i], points[j])])
                    heapq.heappush(pq, (manhattan(points[i], points[j]), i, j))
        
        def kruskal():
            visited = set()
            ans = 0
            dsu = DSU(n)
            
            while pq: 
                weight, u, v = heapq.heappop(pq)
                
                if dsu.union(u, v):
                    ans += weight
                    visited.add(u)
                    visited.add(v)
            
            return ans
        
        create_graph()

        return kruskal()
