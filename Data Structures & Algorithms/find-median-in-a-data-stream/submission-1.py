class MedianFinder:

    def __init__(self):
        # invariant -- if even length of nums read so far, 
        # data is evenly distributed
        # if odd, extra element in minheap 
        self.minheap = []
        self.maxheap = []
    
    def _balance(self):
        if len(self.maxheap) == len(self.minheap):
            return
        
        if (len(self.maxheap) + len(self.minheap))%2 == 0:
            while len(self.maxheap) != len(self.minheap):
                maxtop = -heapq.heappop(self.maxheap)
                heapq.heappush(self.minheap, maxtop)
            return
        
        # odd length datastream 
        while len(self.maxheap) -1 != len(self.minheap):
            maxtop = -heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, maxtop)


    def addNum(self, num: int) -> None:
        heapq.heappush(self.minheap, num)
        mintop = heapq.heappop(self.minheap)
        heapq.heappush(self.maxheap, -mintop)
        
        self._balance()

    def findMedian(self) -> float:
        if len(self.minheap) == len(self.maxheap):
            return (self.minheap[0] + (-1*self.maxheap[0]))/2.0
        
        return -self.maxheap[0]
        