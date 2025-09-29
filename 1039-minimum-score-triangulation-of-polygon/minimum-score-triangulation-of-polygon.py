            if j - i < 2: return 0

            res = float('inf')

            for k in range(i+1, j):
                curr = values[i] * values[j] * values[k]
                res = min(res, curr + dp(i, k) + dp(k, j))
            
            return res
        
            memo[(i, j)] = res
        return dp(0, len(values) - 1)