class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegs = [0] * numCourses
        adj = [[] for i in range(numCourses)]

        for dst, src in prerequisites: 
            adj[src].append(dst)
            indegs[dst] += 1
        
        q = collections.deque()

        for i, indeg in enumerate(indegs):
            if not indeg: q.append(i)
        
        popped = 0
        ans = []
        while q: 
            course = q.popleft()
            ans.append(course)
            popped += 1
            for neigh in adj[course]:
                indegs[neigh] -= 1
                if not indegs[neigh]: q.append(neigh)
        if popped < numCourses: return []
        return ans