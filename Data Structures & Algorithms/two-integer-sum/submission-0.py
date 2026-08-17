class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices_map = {} 
        for index, num in enumerate(nums):
            if num in indices_map:
                indices_map[num].append(index)
            else:
                indices_map[num] = [index]
        
        for index, num in enumerate(nums):
            complement = target - num
            if complement in indices_map: 
                if complement == num: 
                    if len(indices_map[complement]) > 1:
                        return sorted([index, indices_map[complement][1]])
                else:
                    return sorted([index, indices_map[complement][0]])