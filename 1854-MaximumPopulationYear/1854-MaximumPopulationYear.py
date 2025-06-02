# Last updated: 6/2/2025, 9:13:34 PM
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        max_year = 1950
        max_pop = 0

        for year in range(1950, 2051):
            population = 0
            for birth, death in logs:
                if birth <= year < death:
                    population += 1
                
            if population > max_pop:
                max_pop = population
                max_year = year

        return max_year
