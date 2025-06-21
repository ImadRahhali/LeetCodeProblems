# Last updated: 6/21/2025, 3:55:55 PM
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # a / b , b / c, b/d 
        # adj = {a:[[b,equations[0]]], b:[[c,equations[1]],[d,equations[2]]]} store also the value of the equation so we can retrieve it later and m thinking also to store 1/equations[i] for reversed division if asked
        # have a dfs that goes from a given node(queries[j][0]) to a given target(queries[j][1])
        # while in dfs if we aren't none we do res *= adj[neighbor][1]
        # if we reach none then return -1
        # handle edge case if node or target aren't in adj we return 0
        out = []
        adj = {}
        for (Ai, Bi), val in zip(equations,values):
            if Ai not in adj:
                adj[Ai] = []
            if Bi not in adj:
                adj[Bi] = []
            adj[Ai].append((Bi, val))
            adj[Bi].append((Ai, 1 / val))
        def dfs(node, target, visited):
            if node not in adj or target not in adj:
                return -1
            if node == target:
                return 1
            visited.add(node)
            for neighbor, value in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    res = dfs(neighbor, target, visited)
                    if res != -1:
                        return value * res
            return -1
        for Ci, Dj in queries:
            out.append(dfs(Ci, Dj, set()))
        
        return out

