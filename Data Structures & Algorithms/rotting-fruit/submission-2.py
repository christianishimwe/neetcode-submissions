class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        - make sure all oranges are gone
        - iterate through the grid,
        - if this orange if fresh, increase count
        - if it is rotten, put in the deque, with the minute count
        """
        rows = len(grid)
        cols = len(grid[0])
        num_fresh = 0
        q = deque()
        for r in range(rows):
            for c in range(cols):
                val = grid[r][c]
                if val == 1:
                    num_fresh += 1
                elif val == 2:
                    q.append((r, c, 0))
        last_time = 0
        while q:
            r, c, minutes = q.popleft()
            last_time = max(last_time, minutes)
            # check the surroundings
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                row = r + dr
                col = c + dc
                if row < 0 or col < 0 or row >= rows or col >= cols:
                    continue
                if grid[row][col] == 1:
                    # rot this
                    grid[row][col] = 2
                    num_fresh -= 1
                    q.append((row, col, minutes + 1))
        if num_fresh == 0:
            return last_time
        return -1


