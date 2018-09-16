class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        arr=[0]*9
        for line in board:
            for a in line:
                if a!='.':
                    a=int(a)
                    if arr[a-1]>=1:
                        return False
                    else:
                        arr[a-1]+=1
            arr=[0]*9
        
        for i in range(9):
            for j in range(9):
                if board[j][i]!='.':
                    a=int(board[j][i])
                    if arr[a-1]>=1:
                        return False
                    else:
                        arr[a-1]+=1
            arr=[0]*9

        for i in range(3):
            for j in range(3):
                for k in range(i*3,3*i+3):
                    for l in range(j*3,3*j+3):
                        if board[k][l]!='.':
                            a=int(board[k][l])
                            if arr[a-1]>=1:
                                return False
                            else:
                                arr[a-1]+=1
                arr=[0]*9

        return True

s=Solution()
print(s.isValidSudoku([ ["5","3",".",".","7",".",".",".","."],
                        ["6",".",".","1","9","5",".",".","."],
                        [".","9","8",".",".",".",".","6","."],
                        ["8",".",".",".","6",".",".",".","3"],
                        ["4",".",".","8",".","3",".",".","1"],
                        ["7",".",".",".","2",".",".",".","6"],
                        [".","6",".",".",".",".","2","8","."],
                        [".",".",".","4","1","9",".",".","5"],
                        [".",".",".",".","8",".",".","7","9"]]))