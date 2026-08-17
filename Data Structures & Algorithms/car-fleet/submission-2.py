import math
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx == rooty:
            return 

        # always merge x into y
        self.parent[rootx] = rooty
        self.rank[rooty] += 1
        
    def get_count(self):
        count = 0
        for i, elem in enumerate(self.parent):
            if i == elem:
                count += 1
        return count



class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        
        # sort cars in ascending order based on position 
        cars.sort()

        uf = UnionFind(len(position))

        for i in range(len(position) - 1, 0, -1):
            ahead = cars[uf.find(i)]
            behind = cars[i-1]

            if (target - behind[0])/behind[1] <= (target - ahead[0])/ahead[1]:
                uf.union(i-1, i)
        
        return uf.get_count() 