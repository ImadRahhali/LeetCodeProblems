# Last updated: 6/2/2025, 9:39:11 PM
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        pop_changes = [0] * 101
        for birth, death in logs:
            pop_changes[birth - 1950]+=1
            pop_changes[death - 1950]-=1
        
        curr_pop = 0
        max_pop = 0
        max_year = 0

        for i in range(101):
            curr_pop += pop_changes[i]
            if curr_pop > max_pop:
                max_pop = curr_pop
                max_year = 1950 + i
        return max_year

        '''
        #BRUTE FORCE:

        max_pop = 0
        max_year = 1950

        for year in range(1950, 2051):
            population = 0
            for birth, death in logs:
                if birth <= year < death:
                    population += 1
            if population > max_pop:
                max_pop = population
                max_year = year
        return max_year
        
        '''

        
