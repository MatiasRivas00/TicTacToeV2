
def check_win(board):

    matrix = board

    for i in matrix:
        if i[0] == i[1] and i[0] == i[2] and i[0] != " ":
            return True, i[0]
    for j in range(1):
        if matrix[j][0] == matrix[j + 1][1] and matrix[j][0] == matrix[j + 2][2] and matrix[j][0] != ' ':
            return True, matrix[j][0]
    for j in range(1):
        if matrix[j][2] == matrix[j + 1][1] and matrix[j][2] == matrix[j + 2][0] and matrix[j][2] != ' ':
            return True, matrix[j][2]
    for k in range(3):
        Cycle = ""
        for i in range(3):
            Cycle += matrix[i][k]
        if Cycle.find("XXX") != -1:
            return True, "X"
        elif Cycle.find("OOO") != -1:
            return True, "O"

    return False, ""
