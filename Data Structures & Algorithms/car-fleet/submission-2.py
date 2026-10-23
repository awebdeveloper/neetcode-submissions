class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = []

        cars = [[position[i], speed[i]] for i in range(len(speed))];

        cars = sorted(cars, key=lambda x: x[0], reverse=True);

        for car in cars:
            times = (target - car[0]) / car[1]

            if len(stack) == 0 or stack[-1] < times:
                stack.append(times)

        
        return len(stack)
















       