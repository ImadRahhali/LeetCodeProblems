    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        empty = 0
        full = numBottles
        counter = 0
        while numBottles >= numExchange:
            counter += full
            empty += full
            full = empty // numExchange
            empty = empty % numExchange
            numBottles = full + empty
        counter += full
        return counter
