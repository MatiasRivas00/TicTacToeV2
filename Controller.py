import Player
import Board
import Game


class Controller:

    def __init__(self, screen):
        player1 = Player.Player("X")
        player2 = Player.Player("O")
        board = Board.Board()
        self.game = Game.Game(player1, player2, board, screen)

    def controller(self, pos):
        if self.game.player1_turn:
            self.game.play1(pos)
            if self.game.game_over:
                self.game.reset()
            self.bot_play()

    def bot_play(self):
        if not self.game.player1_turn:
            self.game.play2()
            if self.game.game_over:
                self.game.reset()



