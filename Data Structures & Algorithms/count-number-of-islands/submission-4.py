class IslandsSet:
    def __init__(self, rows, cols):
        """
        (1, 2) -> 1 * cols + 2
        (3, 4) -> 3 * cols + 4
        len = rows * cols = 20
        A <- B.  G <- C
        """
        n = rows * cols
        self.rank = [1 for _ in range(n)]
        self.parent = [i for i in range(n)]
    def get_parent(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.get_parent(self.parent[i])
        return self.parent[i]
    def union(self, i, j):
        parent_of_i = self.get_parent(i)
        parent_of_j = self.get_parent(j)
        if parent_of_i == parent_of_j:
            return False
        if self.rank[parent_of_i] < self.rank[parent_of_j]:
            self.parent[parent_of_i] = parent_of_j

        elif self.rank[parent_of_i] > self.rank[parent_of_j]:
            self.parent[parent_of_j] = parent_of_i
        else:
            self.parent[parent_of_i] = parent_of_j
            self.rank[parent_of_j] += 1
        return True  

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # initialzie the IslandsSet
        rows = len(grid)
        cols = len(grid[0])
        num_islands = 0
        grid_sets = IslandsSet(rows, cols)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    num_islands += 1
                    top_r = r - 1
                    top_c = c
                    if top_r >= 0 and grid[top_r][top_c] == "1":
                        # union them and check
                        if grid_sets.union(r * cols + c, top_r * cols + top_c):
                            num_islands -= 1
                    bottom_r = r + 1
                    bottom_c = c
                    if bottom_r < rows and grid[bottom_r][bottom_c] == "1":
                        # union them and check
                        if grid_sets.union(r * cols + c, bottom_r * cols + bottom_c):
                            num_islands -= 1
                    left_r = r
                    left_c = c - 1
                    if left_c >= 0 and grid[left_r][left_c] == "1":
                        # union them and check
                        if grid_sets.union(r * cols + c, left_r * cols + left_c):
                            num_islands -= 1
                    right_r = r
                    right_c = c + 1
                    if right_c < cols and grid[right_r][right_c] == "1":
                        # union them and check
                        if grid_sets.union(r * cols + c, right_r * cols + right_c):
                            num_islands -= 1
                    
        return num_islands


        