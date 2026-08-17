class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mono_dec_stack = collections.deque()
        result = [0] * len(temperatures)
        
        for i, elem in enumerate(temperatures): 
            while mono_dec_stack and elem > temperatures[mono_dec_stack[-1]]:
                index = mono_dec_stack.pop()
                result[index] = i - index
            mono_dec_stack.append(i)
        
        return result

        
