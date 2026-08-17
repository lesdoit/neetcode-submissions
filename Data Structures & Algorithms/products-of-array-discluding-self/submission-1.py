class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cnt_zero = 0 
        for num in nums:
            if num == 0:
                cnt_zero += 1 
        
        if cnt_zero > 1: 
            return [0] * len(nums)
        
        if cnt_zero == 1: 
            prod = 1 
            for num in nums: 
                if num != 0:
                    prod *= num
            
            result = []
            for num in nums:
                if num != 0:
                    result.append(0)
                else:
                    result.append(prod)
            return result

        # division approach 
        prod = 1
        for num in nums: 
            prod *= num 
        
        result = []
        for num in nums:
            result.append(prod//num)
        
        return result

        
