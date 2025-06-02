# Last updated: 6/2/2025, 9:50:05 PM
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        road_changes = [0] * 1001
        for numPassengers, start_point, end_point in trips:
            road_changes[start_point] += numPassengers
            road_changes[end_point] -= numPassengers
        
        curr_passengers = 0

        for i in range(1001):
            curr_passengers += road_changes[i]
            if curr_passengers > capacity:
                return False
        return True
