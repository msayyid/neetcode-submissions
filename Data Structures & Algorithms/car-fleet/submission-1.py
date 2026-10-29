class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # since the front cars wont' let the behind cars pass
        # we will need to process front cars first, 
        # because their speed wont' allow others overtake
        # therefore we pair position and speed of cars and
        # sort them in descending order
        cars = []
        for i in range(len(position)):
            cars.append([position[i], speed[i]])

        # sort (DESC)
        cars = sorted(cars)[::-1]

        fleet = 0
        cur_fleet_time = 0
        for car in cars:
            # calculate time for each car
            # time = distance / speed
            time = (target - car[0]) / car[1]

            # check if car can catch to the fleet in front
            if time <= cur_fleet_time: # do nothing, fleet stays the same, because car catches the fleet ahead
                continue
            else: # if it can't catch up (too slow)
                fleet += 1
                cur_fleet_time = time
        return fleet
