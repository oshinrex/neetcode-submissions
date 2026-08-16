class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_info = [x for x in zip(position, speed)]
        car_info.sort(reverse=True)
        
        fleets = 1
        prevTime = (target - car_info[0][0]) / car_info[0][1]
        for i in range(1, len(car_info)):
            currTime = (target - car_info[i][0]) / car_info[i][1]

            if (currTime > prevTime):
                fleets += 1
                prevTime = currTime

        return fleets

