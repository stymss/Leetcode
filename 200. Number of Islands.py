from typing import List

class Solution:
     # isValid checks for valid boundary
    def isValid(self, grid: List[List[int]], row: int, col: int) -> bool:
        return True if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]) else False

    def numIslands(self, grid: List[List[str]]) -> int:
        # Initialise
        rc, cc = len(grid), len(grid[0])
        visited = [[False]* cc for _ in range(rc)]

        # Traverse the matrix
        island_count = 0
        for r in range(rc):
            for c in range(cc):
                # if the cell is an island, call dfs
                if grid[r][c] == "1" and not visited[r][c]:
                    island_count += 1
                    self.markIslands(grid, visited, r, c)
        return island_count

    def markIslands(self, grid: List[List[str]], visited: List[bool], row: int, col: int):
        # check if dfs should check further
        if not self.isValid(grid, row, col) or grid[row][col] == "0" or visited[row][col]:
            return 

        # mark as visited
        visited[row][col] = True

        # directions
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            next_row, next_col = row + dr, col + dc
            self.markIslands(grid, visited, next_row, next_col)
