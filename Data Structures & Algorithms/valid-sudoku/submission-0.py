class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        - numbers are 1 to 9
        - create sets, in a list
        - for rows, this will be a 1d list, each element is a set
        - for cols, this will be a 1d list, each element is a set
        - for boxes, we will have a 2d list, each element is a set
        - iterate throguh each elemnet [i, j]
        - check row i, and col j for duplicatons
        - check box [i // 3][j // 3]
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                num = board[i][j]
                if num in rows[i]:
                    return False
                if num in cols[j]:
                    return False
                if num in boxes[i // 3][j // 3]:
                    return False
                rows[i].add(num)
                cols[j].add(num)
                boxes[i // 3][j // 3].add(num)   
        return True    