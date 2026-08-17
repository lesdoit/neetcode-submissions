class Solution:

    def encode(self, strs: List[str]) -> str:
        # use a number and delimiter to indicate how many 
        # characters to read 
        encoded = ""
        for s in strs:
            n = len(s)
            encoded += str(n) 
            encoded += ':'
            encoded += s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        n = len(s)
        while i < n:
            num = ""
            if s[i].isdigit():
                while s[i].isdigit():
                    num += s[i]
                    i+=1
                num = int(num)
            
            i+=1
            
            word = ""
            j = i + num
            while i < j: 
                word += s[i]
                i+=1
            decoded.append(word)
            
            
        return decoded
