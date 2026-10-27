from math import prod
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # first traverse and the whole array and 
        # create segments that are non zero 

        sliced = []
        cur = []
        res = float('-inf')
        for num in nums: 
            res = max(res, num)
            if num == 0:
                if cur: 
                    sliced.append(cur)
                cur = []
            else:
                cur.append(num)
        if cur: 
            sliced.append(cur)
        
        # for each segment, 
        for sub in sliced: 
            # Single element segment
            if len(sub) == 1:
                res = max(res, sub[0])
                continue

            neg_indices = [idx for idx, val in enumerate(sub) if val < 0]

            # Even count: entire product is positive
            if len(neg_indices) % 2 == 0:
                res = max(res, prod(sub))
            else:
                # Odd count: drop first negative OR drop last negative
                first_neg, last_neg = neg_indices[0], neg_indices[-1]
                
                # Suffix after first negative & Prefix before last negative
                suffix = prod(sub[first_neg + 1:]) if first_neg + 1 < len(sub) else float('-inf')
                prefix = prod(sub[:last_neg]) if last_neg > 0 else float('-inf')
                
                res = max(res, suffix, prefix)
        return res
        