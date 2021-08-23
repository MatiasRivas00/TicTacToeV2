import Coordinates
import CheckWin
import Draw
import MiniMax


class Game:
    def __init__(self, player1, player2, board, screen):
        self.player1 = player1
        self.player2 = player2
        self.board = board
        self.screen = screen
        self.player1_turn = True
        self.game_over = False

    def reset(self):
        self.board.reset_board()
        Draw.draw_board(self.screen)

    def play1(self, pos):
        mark = self.player1.mark
        x, y = Coordinates.new_cord(pos[0], pos[1])
        self.board.put(mark, x, y)
        tx, ty = Coordinates.fig_center(x, y)
        Draw.draw_mark(mark, self.screen, (tx, ty))
        self.player1_turn = False
        self.game_status()

    def play2(self):
        mark = self.player2.mark
        x, y = MiniMax.best_move(self.board.get_board())
        self.board.put(mark, x, y)
        tx, ty = Coordinates.fig_center(x, y)
        Draw.draw_mark(mark, self.screen, (tx, ty))
        self.player1_turn = True
        self.game_status()

    def game_status(self):
        if self.board.is_full() or CheckWin.check_win(self.board.get_board())[0]:
            self.game_over = True
