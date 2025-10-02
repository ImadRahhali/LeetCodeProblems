                numExchange += 1
            #Drink
            else:
                counter += full
                empty += full
                full = 0
            numBottles = full + empty
        counter += full
        return counter