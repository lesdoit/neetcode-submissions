class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # hierholzer's algo 
        # an eulerian path exists iff exactly two vertices have 
        # an odd degree (regardless of directed or undirected graph) and every other 
        # vertex has an even degree 

        # Fundamentally it is a DFS algo. 
        tickets.sort(reverse=True)
        adj = defaultdict(list)
        for ticket in tickets:
            adj[ticket[0]].append(ticket[1])
        
        print(f"Adj: {adj}")

        res = []
        def dfs(src):
            while adj[src]:
                next_airport = adj[src].pop()
                dfs(next_airport)
            res.append(src)
        
        dfs("JFK")
        return res[::-1]
