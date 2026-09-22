class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            test = list()
            for j in range(9):
                if board[i][j] != ".":
                    test.append(board[i][j])
            if len(set(test)) != len(test):
                return False

        for j in range(9):
            test = list()
            for i in range(9):
                if board[i][j] != ".":
                    test.append(board[i][j])
            if len(set(test)) != len(test):
                return False

        for t in range(3):
            for w in range(3):
                test2 = list()
                for i in range(3*t,3*(t+1)):
                    for j in range(3*w,3*(w+1)):
                        if board[i][j] != ".":
                            test2.append(board[i][j])
                            print(board[i][j])
                    if len(set(test2)) != len(test2):
                        return False
                print(test2)
                print(",")
            print(",")
        
        return True
