from typing import List

class Solution:
    # isValid checks for valid boundary
    def isValid(self, image: List[List[int]], row: int, col: int) -> bool:
        return True if row >= 0 and row < len(image) and col >= 0 and col < len(image[0]) else False
    
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Initialise
        rc, cc = len(grid), len(grid[0])
        visited = [[False]* cc for _ in range(rc)]

        # Traverse the matrix
        for r in range(rc):
            for c in range(cc):
                # if the cell is an island, call dfs
                if grid[r][c] == 1:
                    return self.traverseIsland(grid, visited, r, c)
        return 0
    
    def traverseIsland(self, grid: List[List[int]], visited: List[bool], row: int, col: int):
        if not self.isValid(grid, row, col) or grid[row][col] == 0 or visited[row][col]:
            return 0

        visited[row][col] = True

        # this cell will contribute 4 to the perimeter
        island_perimeter = 4

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            next_row, next_col = row + dr, col + dc
            if self.isValid(grid, next_row, next_col) and grid[next_row][next_col] == 1:
                # Reduce perimeter for adjacent land
                island_perimeter -= 1
            # Recur for the next cell
            island_perimeter += self.traverseIsland(grid, visited, next_row, next_col)

        return island_perimeter