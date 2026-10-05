class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Kahn's algo for topo and cycle detection (BFS topo)
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for dest, src in prerequisites: 
            adj[src].append(dest)
            indegree[dest] += 1

        q = collections.deque() 
        for i, indeg in enumerate(indegree): 
            if indeg == 0:
                q.append(i)
        
        popped = 0
        while q: 
            course = q.popleft()
            popped += 1
            for neigh in adj[course]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0: 
                    q.append(neigh)
        return popped == numCourses

