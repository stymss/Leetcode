from typing import List
from collections import defaultdict

class Pair:
    def __init__(self, neighbour, weight):
        self.neighbour = neighbour
        self.weight = weight

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # create adjacency list representation for this using equations = [["a","b"],["b","c"]] and values = [2.0,3.0],
        graph = defaultdict(list)
        for (a, b), value in zip(equations, values):
            graph[a].append(Pair(b, value))
            graph[b].append(Pair(a, 1/value))

        # process quries (we can use bfs or dfs)
        # queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
        queries_results = []
        for query in queries:
            queries_results.append(self.evalEq(query[0], query[1], set(), graph))
        
        return queries_results

    def evalEq(self, start_node, end_node, visited, graph) -> float:
        # for cases like ["x","x"] where "x" is not in the graph
        if start_node not in graph or end_node not in graph:
            return -1.0
        # for cases like ["a","a"] which is a self cycle
        if start_node == end_node:
            return 1.0
        
        # mark visited
        visited.add(start_node)

        # check neighbours
        for pair in graph[start_node]:
            neighbour, weight = pair.neighbour, pair.weight
            if neighbour not in visited:
                result = self.evalEq(neighbour, end_node, visited, graph)
                if result != -1:
                    return result * weight
                

        # unmark visited for next query
        visited.remove(start_node)
        return -1.0