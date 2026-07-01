class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range (len(board)):
            empty_dict = {}
            for j in range(len(board)):
                if board[i][j] == "." :
                    pass
                else:
                    if board[i][j] in empty_dict:
                        return False
                    else:
                        empty_dict[board[i][j]] = 1

        for i in range (len(board)):
            empty_dict = {}
            for j in range(len(board)):
                if board[j][i] == "." :
                    pass
                else:
                    if board[j][i] in empty_dict:
                        return False
                    else:
                        empty_dict[board[j][i]] = 1

        empty_dict = {}
        for i in range(3):
            for j in range(3):
                if board[i][j] == "." :
                    pass
                else:
                    if board[i][j] in empty_dict:
                        return False
                    else:
                        empty_dict[board[i][j]] = 1

        empty_dict = {}
        for i in range(3):
            for j in range(3):
                j = j + 3
                if board[i][j] == "." :
                    pass
                else:
                    if board[i][j] in empty_dict:
                        return False
                    else:
                        empty_dict[board[i][j]] = 1

        empty_dict = {}
        for i in range(3):
            for j in range(3):
                j = j + 6
                if board[i][j] == "." :
                    pass
                else:
                    if board[i][j] in empty_dict:
                        return False
                    else:
                        empty_dict[board[i][j]] = 1

        empty_dict = {}
        for i in range(3):
            i = i+3
            for j in range(3):
                if board[i][j] == "." :
                    pass
                else:
                    if board[i][j] in empty_dict:
                        return False
                    else:
                        empty_dict[board[i][j]] = 1

        empty_dict = {}
        for i in range(3):
            i = i+3
            for j in range(3):
                j = j+3
                if board[i][j] == "." :
                    pass
                else:
                    if board[i][j] in empty_dict:
                        return False
                    else:
                        empty_dict[board[i][j]] = 1

        empty_dict = {}
        for i in range(3):
            i = i+3
            for j in range(3):
                j = j+6
                if board[i][j] == "." :
                    pass
                else:
                    if board[i][j] in empty_dict:
                        return False
                    else:
                        empty_dict[board[i][j]] = 1


        empty_dict = {}
        for i in range(3):
            i = i+6
            for j in range(3):
                if board[i][j] == "." :
                    pass
                else:
                    if board[i][j] in empty_dict:
                        return False
                    else:
                        empty_dict[board[i][j]] = 1

        empty_dict = {}
        for i in range(3):
            i = i+6
            for j in range(3):
                j = j + 3
                if board[i][j] == "." :
                    pass
                else:
                    if board[i][j] in empty_dict:
                        return False
                    else:
                        empty_dict[board[i][j]] = 1

        empty_dict = {}
        for i in range(3):
            i = i+6
            for j in range(3):
                j = j + 6
                if board[i][j] == "." :
                    pass
                else:
                    if board[i][j] in empty_dict:
                        return False
                    else:
                        empty_dict[board[i][j]] = 1
            
        return True