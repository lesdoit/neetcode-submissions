import bisect

class TimeMap:

    def __init__(self):
        self.d = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        l = self.d[key]
        
        def check(mid):
            return 1 if l[mid][0] <= timestamp else 0
        
        def bs():
            lo, hi = 0, len(l) - 1
            ans = -1
            while lo <= hi:
                mid = lo + (hi-lo)//2
                if check(mid):
                    ans = mid 
                    lo = mid + 1
                else:
                    hi = mid - 1
            
            return l[ans][1] if ans != -1 else ""
        
        return bs()
        
