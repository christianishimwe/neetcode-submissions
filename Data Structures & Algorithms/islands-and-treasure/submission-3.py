class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        - collect all the ones with 0s, 
        - BFS from these elements
        - and append those to the deque
        """
        #grid = [[2147483647, 2147483647, 0, -1]]
        INF = 2147483647
        d = deque()
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    d.append((r, c))
        while d:
            r, c = d.popleft()
            # check the four directions for land
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for dr, dc in directions:
                row = r + dr
                col = c + dc
                if row < 0 or col < 0 or row >= rows or col >= cols:
                    continue
                if grid[row][col] == INF:
                    # add it
                    grid[row][col] = 1 + grid[r][c]
                    d.append((row, col))
        
        