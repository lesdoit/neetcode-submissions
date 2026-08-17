import string

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        resLen = 0
        # defaults count to 0 for absent keys
        freq = collections.defaultdict(int)
        alphabet = list(string.ascii_uppercase)
        
        while r < len(s):
            freq[s[r]] += 1
            
            max_freq = 0
            for ch in alphabet: 
                max_freq = max(max_freq, freq[ch])
            
            window_l = (r - l + 1)
            
            if max_freq + k >= window_l:
                resLen = max(resLen, window_l)
            else: 
                freq[s[l]] -= 1
                l += 1

            r += 1
        return resLen