class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = [0] * len(nums)
        postfix_prod = [0] * len(nums)

        prod = 1
        for idx, num in enumerate(nums): 
            prod *= num
            prefix_prod[idx] = prod
        
        prod = 1
        for i in range(len(nums)-1, -1, -1): 
            prod *= nums[i]
            postfix_prod[i] = prod
        
        result = []
        for i in range(len(nums)):
            pre, post = 1, 1
            if i > 0:
                pre *= prefix_prod[i-1]
            if i < len(nums) - 1:
                post *= postfix_prod[i+1]
            result.append(pre*post)
        
        return result

        
