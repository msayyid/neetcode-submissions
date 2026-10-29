class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair each car's position with its speed.
        cars = []
        for i in range(len(position)):
            cars.append([position[i], speed[i]])

        # Sort cars from closest to the target to furthest.
        # We process front cars first because cars behind cannot pass them.
        cars = sorted(cars)[::-1]

        fleet = 0
        cur_fleet_time = 0

        for car in cars:
            # Calculate how long this car would take to reach the target alone.
            # time = distance / speed
            time = (target - car[0]) / car[1]

            # If this car reaches earlier or at the same time as the fleet ahead,
            # it catches that fleet, so it does not create a new fleet.
            if time <= cur_fleet_time:
                continue

            # Otherwise, this car is too slow to catch the fleet ahead,
            # so it becomes a new fleet.
            fleet += 1
            cur_fleet_time = time

        return fleet