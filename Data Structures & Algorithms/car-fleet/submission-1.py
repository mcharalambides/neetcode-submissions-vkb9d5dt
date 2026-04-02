class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = sorted(zip(position, speed), key=lambda x: -x[0])

        fleets = 0
        curr_slowest = 0
        for pos, spd in cars:
            time = (target - pos) / spd

            if time > curr_slowest:
                fleets += 1
                curr_slowest = time

        return fleets

