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
        # now let's try to begin from the very ends
        def dfs(i, j):
            pacific, atlantic = result[i][j]
            # check the four corners of where to dfs next
            if pacific and atlantic:
                output.add((i, j))
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                row = i + dr
                col = j + dc
                if row < 0 or col < 0 or row >= rows or col >= cols:
                    continue
                # check if we haven't done this before
                new_pacific, new_atlantic = result[row][col]
                # else mark this is the heihg is just right
                if heights[i][j] > heights[row][col]:
                    continue
                should_recurse = False
                '''
                if i == 0 and j == 4:
                    print("here")
                    print(f"row = {row}, col={col}")
                    print(f"new_p={new_pacific}, new_a={new_atlantic}")
                '''
                if not new_pacific and pacific:
                    should_recurse = True
                    result[row][col][0] = True
                if not new_atlantic and atlantic:
                    should_recurse = True
                    result[row][col][1] = True
                # recurse from here too
                if should_recurse:
                    dfs(row, col)
        rows = len(heights)
        cols = len(heights[0])
        result = [[[False, False] for _ in range(cols)] for _ in range(rows)]
        output = set()
        for r in range(rows):
            result[r][0][0] = True
            result[r][cols - 1][1] = True
        for c in range(cols):
            result[0][c][0] = True
            result[rows - 1][c][1] = True
        # now dfs from those areas
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)            
        output = [[i, j] for i, j in output]
        return output


    