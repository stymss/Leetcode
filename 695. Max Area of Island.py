from typing import List

class Solution:
    # isValid checks for valid boundary
    def isValid(self, image: List[List[int]], row: int, col: int) -> bool:
        return True if row >= 0 and row < len(image) and col >= 0 and col < len(image[0]) else False
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Initialise
        rc, cc = len(grid), len(grid[0])
        visited = [[False]* cc for _ in range(rc)]

        # Traverse the matrix
        max_island_area = 0
        for r in range(rc):
            for c in range(cc):
                # if the cell is an island, call dfs
                if grid[r][c] == 1 and not visited[r][c]:
                    island_area =  self.traverseIsland(grid, visited, r, c)
                    max_island_area = max(max_island_area, island_area)
        return max_island_area
    
    def traverseIsland(self, grid: List[List[int]], visited: List[bool], row: int, col: int):
        if not self.isValid(grid, row, col) or grid[row][col] == 0 or visited[row][col]:
            return 0

        # visit it
        visited[row][col] = True

        # this cell will contribute 1 to the area
        island_cell_count = 1

        # check all 4 directions
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            next_row, next_col = row + dr, col + dc
            island_cell_count += self.traverseIsland(grid, visited, next_row, next_col)

        return island_cell_count