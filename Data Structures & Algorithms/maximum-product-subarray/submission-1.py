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
            negs = sum(1 for i in sub if i<0)
            prod = 1
            need = negs if negs%2 == 0 else negs - 1 
            negs = 0
            j = 0

            for i in range(len(sub)):
                prod *= sub[i]
                if sub[i] < 0:
                    negs += 1
                    while negs > need:
                        prod //= sub[j]
                        if sub[j] < 0:
                            negs -= 1
                        j += 1
                if j <= i:
                    res = max(res, prod)
        return res
        