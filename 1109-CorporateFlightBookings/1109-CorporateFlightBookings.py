# Last updated: 6/2/2025, 10:21:05 PM
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        seat_updates = [0] * n
        for first, last, seats in bookings:
            seat_updates[first - 1] += seats
            if last < n:
                seat_updates[last] -= seats
        answer = []
        curr_seats = 0
        for i in range(n):
            curr_seats += seat_updates[i]
            answer.append(curr_seats)
        return answer