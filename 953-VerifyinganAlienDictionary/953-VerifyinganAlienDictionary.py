# Last updated: 6/7/2025, 12:52:45 PM
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {char: index for index, char in enumerate(order)}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]

            for j in range(len(w1)):
                if j == len(w2):
                    return False     
                
                if order_map[w1[j]] < order_map[w2[j]]:
                    break

                elif order_map[w1[j]] > order_map[w2[j]]:
                    return False

        return True  


