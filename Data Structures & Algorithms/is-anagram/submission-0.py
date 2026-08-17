class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
            
        for char in t:
            if char in freq:
                freq[char] -= 1
            else:
                return False
        
        # check that all values in the map are equal to 0
        for k, v in freq.items():
            if v > 0:
                return False 
        
        return True