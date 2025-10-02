class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        counter = numBottles
        empty = numBottles

        while empty >= numExchange:
            counter += 1
            empty -= numExchange - 1
            numExchange += 1
        return counter