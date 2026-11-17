class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        if len(words) == 1: return words[0]
        adj = collections.defaultdict(list)
        indegrees = collections.defaultdict(int)
        
        def get_idx(w1, w2):
            for i in range(min(len(w1), len(w2))):
                if w1[i] != w2[i]: return i
            return min(len(w1), len(w2))

        for i in range(len(words) - 1):
            
            for ch in words[i]:
                adj[ch]
                indegrees[ch]
            
            for ch in words[i+1]:
                adj[ch]
                indegrees[ch]

            idx = get_idx(words[i], words[i+1])
            # print(f"idx: {idx}")
            
            if len(words[i]) > len(words[i+1]) and len(words[i+1]) == idx: return ""
            if len(words[i+1]) > len(words[i]) and len(words[i]) == idx: continue
            if len(words[i]) == len(words[i+1]) and len(words[i]) == idx: continue
            adj[words[i][idx]].append(words[i+1][idx])
            indegrees[words[i+1][idx]] += 1
        
        # kahn's algo

        q = collections.deque()
        
        for ch, indegree in indegrees.items():
            # print(f"ch: {ch}, indeg: {indegree}")
            if not indegree: 
                q.append(ch)
        
        ans = []
        visited = set()
        while q:
            char = q.popleft()
            ans.append(char)
            visited.add(char)

            for nei in adj[char]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    if nei in visited: return ""
                    q.append(nei)
        
        if len(visited) != len(adj): return ""
        return ''.join(ans)

