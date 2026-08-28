class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        # aaa -> [a, a, a], [aa, a], [a, aa], [aaa]
        # aab -> [a, a, b], [aa, b], []
        # bab -> [b, a, b], [bab]
        # a -> [a]
        # aa -> [a, a], [aa]
        # Do not further divide the left side of the string. 
        # Only keep splitting the right side. 
        # only insert a cutpoint if left side is a palindrome 
        
        def rec(s, start, end, res):
            # base case 
            if start == end - 1:
                res.append([s[start:end]])
            else: 
                for i in range(start+1, end+1):
                    if s[start:i] == ''.join(reversed(s[start:i])):
                        left = [s[start:i]]
                        right_res = []
                        rec(s, i, end, right_res)
                        # print(f"i: {i}, left: {left}, right: {right_res}")
                        if i == end: 
                            res.append(left) 
                        else: 
                            for parts in right_res:
                                res.append(left + parts)
                return res       
        
        res = []
        rec(s, 0, len(s), res)
        print(f"res: {res}")
        return res