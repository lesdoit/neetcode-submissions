import string 

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        def rec(digits, cur, mp, res, partial): 
            # base case 
            if cur == len(digits):
                res.append(''.join(partial))
            else: 
                dig = int(digits[cur])
                if dig != 1 or dig != 0: 
                    for ch in mp[dig]:
                        rec(digits, cur + 1, mp, res, partial + [ch])
                else: 
                    rec(digits, cur + 1, mp, res, list(partial))
        
        if not digits: return []
        res = []
        mp = {0: "", 1: "", 2: "abc", 3: "def", 4: "ghi", 5: "jkl", \
                6: "mno", 7: "pqrs", 8: "tuv",  9:"wxyz"}
        rec(digits, 0, mp, res, [])
        return res