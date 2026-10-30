
class IslandsSet:
    def __init__(self, grid):
        """
        (1, 2) -> 1 * cols + 2
        (3, 4) -> 3 * cols + 4
        len = rows * cols = 20
        A <- B.  G <- C
        """
        rows = len(grid)
        cols = len(grid[0])
        n = rows * cols
        self.rank = [1 for _ in range(n)]
        self.parent = [i for i in range(n)]
        self.area = [0 for _ in range(n)]
        for r in range(rows):
            for c in range(cols):
                self.area[(r * cols) + c] = grid[r][c]
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
            self.area[parent_of_j] += self.area[parent_of_i]

        elif self.rank[parent_of_i] > self.rank[parent_of_j]:
            self.parent[parent_of_j] = parent_of_i
            self.area[parent_of_i] += self.area[parent_of_j]
        else:
            self.parent[parent_of_i] = parent_of_j
            # update the area
            self.area[parent_of_j] += self.area[parent_of_i]
            # the rest
            self.rank[parent_of_j] += 1
        return True 

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        islands = IslandsSet(grid)
        rows = len(grid)
        cols = len(grid[0])
        """
        islands.union(0, 1)
        row = 0
        col = 1
        neighbor_row = 0
        neighbor_col = 2
        islands.union(row * cols + col, neighbor_row * cols + neighbor_col)
        print(islands.parent)
        print(islands.area)
        row = 0
        col = 2
        neighbor_row = 1
        neighbor_col = 2
        islands.union(row * cols + col, neighbor_row * cols + neighbor_col)
        print(islands.parent)
        print(islands.area)
        """
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    continue
                elem_index = r * cols + c
                directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    if row < 0 or col < 0 or row >= rows or col >= cols:
                        continue
                    if grid[row][col] == 0:
                        continue
                    neighbor_index = row * cols + col
                    #print(elem_index)
                    #print(neighbor_index)
                    islands.union(elem_index, neighbor_index)
        #print(islands.area)
        return max(islands.area)
        