class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(speed)):
            cars.append([position[i], speed[i]])

        cars.sort(reverse=True) 
        print(cars)
        # now we got the cars closest to target -> furthest from target

        stack = []
        # stack will store the arrival times of fleets
        for car in cars:
            # print(cars[0])
            time = (target - car[0]) / car[1]
            if stack and time <= stack[-1]:
                stack.pop()
            stack.append(time)
        return len(stack)