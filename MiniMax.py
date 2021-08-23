import CheckWin
import math
bestMove = {}
save_result = {}
count = 0
pruning = False


def best_move(board):
    global pruning
    BoardMatrix = board
    bestScore = -math.inf
    move = (0, 0)
    for i in range(3):
        for j in range(3):
            if BoardMatrix[i][j] == " ":
                try:
                    return bestMove[str(board)]
                except:
                    BoardMatrix[i][j] = "O"
                    score = minimax(BoardMatrix, 0, False, -math.inf, math.inf)
                    BoardMatrix[i][j] = " "
                    if score > bestScore:
                        bestScore = score
                        move = (i, j)
    bestMove[str(board)] = move
    pruning = True
    return move


def minimax(board, depth, maximizing, alpha, beta):
    global count
    global pruning
    count += 1
    print(depth, count)
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
                    try:
                        score = save_result[str(board)]
                    except:
                        score = minimax(board, depth + 1, False, alpha, beta) - depth - 1
                        save_result[str(board)] = score
                    board[i][j] = " "
                    bestScore = max(score, bestScore)
                    alpha = max(alpha, score)
                    if beta <= alpha and pruning:
                        break
        return bestScore
    else:
        bestScore = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    try:
                        score = save_result[str(board)]
                    except:
                        score = minimax(board, depth + 1, True, alpha, beta) + depth + 1
                        save_result[str(board)] = score
                    board[i][j] = " "
                    bestScore = min(bestScore, score)
                    beta = min(beta, score)
                    if beta <= alpha and pruning:
                        break
        return bestScore


def is_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True
