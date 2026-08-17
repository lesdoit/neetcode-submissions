class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = -1 * heapq.heappop(stones)
            x = -1 * heapq.heappop(stones)
            if x != y:
                heapq.heappush(stones, -1*abs(x - y))
        
        if stones:
            return -1*stones[0]
        return 0
