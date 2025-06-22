# Last updated: 6/22/2025, 10:09:44 AM
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = [] #store indexes instead of values

        for i in range(n):
            curr = temperatures[i]
            while stack and curr > temperatures[stack[-1]]:
                idx = stack.pop()
                answer[idx] = i - idx
            stack.append(i)
        
        return answer
