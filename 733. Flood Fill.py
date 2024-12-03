from typing import List
from collections import deque

class Pair:
    def __init__(self, row, col):
        self.row = row
        self.col = col 

class Solution:
    # isValid checks for valid boundary
    def isValid(self, image: List[List[int]], row: int, col: int) -> bool:
        return True if row >= 0 and row < len(image) and col >= 0 and col < len(image[0]) else False
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Initialise
        rc, cc = len(image), len(image[0])
        visited = [[False]* cc for _ in range(rc)]

        # Store current cell color and mark the cell with the new color
        cur_cell_color = image[sr][sc]
        image[sr][sc] = color


        # Add to queue and mark visited
        q = deque()
        q.append(Pair(sr, sc))
        visited[sr][sc] = True

        # create coordinates for 4 directions
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # do bfs
        while q:
            pair = q.popleft()
            row, col = pair.row, pair.col 

            # check in all 4 directions for flood fill
            for i in range(4):
                next_row, next_col = row + dirs[i][0], col + dirs[i][1]

                # check if this is within boundary and holds the original cell color
                if self.isValid(image, next_row, next_col) and image[next_row][next_col] == cur_cell_color and not visited[next_row][next_col]:
                    visited[next_row][next_col] = True 
                    image[next_row][next_col] = color
                    q.append(Pair(next_row, next_col))

        return image