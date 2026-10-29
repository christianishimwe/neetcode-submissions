class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        - use dfs
        - dfs starts at each cell
        - if the cell is 0, it returns 0
        - if the cell is seen already, also return 0
        - otherwise keep counting and find teh max
        """
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0
        seen = set()
        for r in range(rows):
            for c in range(cols):
                if (r, c) in seen:
                    continue
                if grid[r][c] == 0:
                    continue
                max_area = max(max_area, self.dfs(r, c, seen, grid))
        return max_area


    def dfs(self, r, c, seen, grid) -> int:
        rows = len(grid)
        cols = len(grid[0])
        if grid[r][c] == 0:
            return 0
        if (r, c) in seen:
            return 0
        # mark this seen here, we just saw this
        seen.add((r, c))
        # go all up
        # count the area
        tot_area = 1
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        for dr, dc in directions:
            row = r + dr
            col = c + dc
            if row < 0 or row >= rows or col < 0 or col >= cols:
                continue
            if (row, col) in seen:
                continue
            tot_area += self.dfs(row, col, seen, grid)
        return tot_area