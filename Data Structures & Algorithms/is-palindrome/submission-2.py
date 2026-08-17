class Solution:
    def cleanup(self, s: str) -> str: 
        clean_s = ''.join(ch for ch in s.lower() if ch.isalnum())
        return clean_s
    
    def isPalindrome(self, s: str) -> bool:
        clean_s = self.cleanup(s)
        if len(clean_s) <= 1: 
            return True
        print(clean_s)
        
        reverse = clean_s[::-1] 
        return reverse == clean_s