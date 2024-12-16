
from collections import deque
from collections import defaultdict
from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Create graph
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Create vis array
        vis = [False]*n

        # Mark the source as visited
        vis[source] = True

        # Use bfs
        q = deque([source])
        is_dest_found = False

        # edge case, where src == dest
        if source == destination:
            return True

        while q:
            node = q.popleft()

            # check neighbours
            for neighbor in graph[node]:
                if neighbor == destination:
                    is_dest_found = True
                    break
                else:
                    if not vis[neighbor]:
                        q.append(neighbor)
                        vis[neighbor] = True
        
        return is_dest_found