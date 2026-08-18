class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #use hashset for constant lookup time
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set) # key = (r//3, c//3)
        #board = 3x3 board of 3x3 boxes -> floor division of row/col indices by 3 would get the indices of the boxes
        
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in rows[row] or board[row][col] in cols[col] or board[row][col] in boxes[(row // 3, col // 3)]: #validation
                    return False
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                boxes[(row // 3, col // 3)].add(board[row][col])

        return True


