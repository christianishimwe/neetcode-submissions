# we will need a union set
"""
- have a union set
- for each head, store two values, does it touch the ocean x, or y
- when you merge, also do the AND to make sure the head has the relevant info
- union sounds like a wrong idea
- start from the boundary cells, go to higher level cells and markt those
- if this value you want to find was already marked, then stop and return
"""

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        

        def dfs(i, j, visit, prev_height):
            if (i, j) in visit:
                return
            if i < 0 or j < 0 or i == rows or j == cols:
                return
            # if this i not the best height upgrade
            if heights[i][j] < prev_height:
                return
            # go all the corners
            visit.add((i, j))
            new_height = heights[i][j]
            dfs(i + 1, j, visit, new_height)
            dfs(i - 1, j, visit, new_height)
            dfs(i, j + 1, visit, new_height)
            dfs(i, j - 1, visit, new_height)
        rows = len(heights)
        cols = len(heights[0])
        pac = set()
        atl = set()
        for r in range(rows):
            dfs(r, 0, pac, 0)
            dfs(r, cols - 1, atl, 0)
        for c in range(cols):
            dfs(0, c, pac, 0)
            dfs(rows - 1, c, atl, 0)
        # go through all and check what's in both
        result = []
        for i in range(rows):
            for j in range(cols):
                if (i, j) in pac and (i, j) in atl:
                    result.append([i, j])
        return result







