class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        my_list = []
        for i in range(len(position)):
            my_list.append([position[i], speed[i]])

        my_list = sorted(my_list)[::-1]

        fleets = 0
        current_fleet_time = 0
        print(my_list[0][0])
        for car in my_list:
            time = (target - car[0]) / car[1]

            if time > current_fleet_time:
                fleets += 1
                current_fleet_time = time
            # else:
            #     fleets += 1

        return fleets