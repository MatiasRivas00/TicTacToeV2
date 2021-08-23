import CheckWin
import math


def best_move(board):
    BoardMatrix = board
    bestScore = -math.inf
    move = (0, 0)
    for i in range(3):
        for j in range(3):
            if BoardMatrix[i][j] == " ":
                BoardMatrix[i][j] = "O"
                score = minimax(BoardMatrix, 0, False, -math.inf, math.inf)
                BoardMatrix[i][j] = " "
                if score > bestScore:
                    bestScore = score
                    move = (i, j)
    return move


def minimax(board, depth, maximizing, alpha, beta):
    scores = {"X": -10, "O": 10, "tie": 0}
    result, pl = CheckWin.check_win(board)
    if result:
        return scores[pl]
    elif is_full(board):
        return 0

    elif maximizing:
        bestScore = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False, alpha, beta) - depth - 1
                    board[i][j] = " "
                    bestScore = max(score, bestScore)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break
        return bestScore
    else:
        bestScore = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True, alpha, beta) + depth + 1
                    board[i][j] = " "
                    bestScore = min(bestScore, score)
                    beta = min(beta, score)
                    if beta <= alpha:
                        break
        return bestScore


def is_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True
