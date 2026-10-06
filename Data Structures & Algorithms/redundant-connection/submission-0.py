
class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        xP = self.find(x)
        yP = self.find(y)
        if xP == yP: 
            return False 
        
        if self.rank[xP] < self.rank[yP]: 
            xP, yP = yP, xP
        
        self.parent[yP] = xP
        
        if self.rank[xP] == self.rank[yP]:
            self.rank[xP] += 1
        
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # undirected graph cycle detection 
        dsu = DSU(len(edges))
        ans = []
        for n1, n2 in edges:
            if not dsu.union(n1-1, n2-1): 
                ans.append(n1)
                ans.append(n2)
        
        return ans