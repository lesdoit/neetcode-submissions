class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        
        # sort cars in ascending order based on position 
        cars.sort()

        stack = collections.deque()
        stack.append(cars[-1])
        for i in range(len(position) - 2, -1, -1):
            ahead = stack[-1]
            behind = cars[i]

            if (target - behind[0])/behind[1] > (target - ahead[0])/ahead[1]:
                stack.append(cars[i])
        
        return len(stack)