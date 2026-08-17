class Solution:
    def cleanup(self, s: str) -> str: 
        clean_s = ''.join(ch for ch in s.lower() if ch.isalnum())
        return clean_s
    
    def isPalindrome(self, s: str) -> bool:
        clean_s = self.cleanup(s)
        if len(clean_s) <= 1: 
            return True
        print(clean_s)
        # two ptr approach 
        i, j = 0, len(clean_s) - 1
        while i <= j: 
            if clean_s[i] != clean_s[j]:
                return False
            else:
                i += 1
                j -= 1
        
        return True