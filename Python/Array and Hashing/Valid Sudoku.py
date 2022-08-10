import collections
class Solution:
    def isValidSudoku(self, board) -> bool:
        hashset = []
        #check rows and 
        for row in board:
            for ele in row:
                if ele == ".":
                    continue
                elif ele not in hashset:
                    hashset.append(ele)
                else:
                    return False
            hashset.clear()
            
        # check columns
        for i in range(9):
            for column in board:
                if column[i] == ".":
                    continue
                elif column[i] not in hashset:
                    hashset.append(column[i])
                else:
                    return False
            hashset.clear()
        
        # check sub-boxes 3x3
        squares = collections.defaultdict(set)  # key = (r /3, c /3)
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                elif board[i][j] not in squares[(i // 3, j // 3)]:
                    squares[(i // 3, j // 3)].add(board[i][j])
                else:
                    return False
        return True

board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

a = Solution()
print(a.isValidSudoku(board))