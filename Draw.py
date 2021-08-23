import pygame
import numpy as np

BLACK = (0, 0, 0)
LINE_BOARD_WIDTH = 10
FIG_LINE_WIDTH = 4
LENGTH = 16
BACKGROUND = (255, 255, 255)


def draw_board(screen):
    screen.fill(BACKGROUND)
    pygame.draw.line(screen, BLACK, (200, 0), (200, 600), LINE_BOARD_WIDTH)
    pygame.draw.line(screen, BLACK, (400, 0), (400, 600), LINE_BOARD_WIDTH)
    pygame.draw.line(screen, BLACK, (0, 200), (600, 200), LINE_BOARD_WIDTH)
    pygame.draw.line(screen, BLACK, (0, 400), (600, 400), LINE_BOARD_WIDTH)


def draw_x_from_center_point(screen, center):
    x0, y0 = center
    x, y = LENGTH / 2 / np.sqrt(2), LENGTH / 2 / np.sqrt(2)
    start_1 = (x0 - x, y0 - y)
    end_1 = (x0 + x, y0 + y)
    start_2 = (x0 - x, y0 + y)
    end_2 = (x0 + x, y0 - y)

    pygame.draw.line(screen, BLACK, start_1, end_1, FIG_LINE_WIDTH)
    pygame.draw.line(screen, BLACK, start_2, end_2, FIG_LINE_WIDTH)


def draw_o_from_center_point(screen, center):
    pygame.draw.circle(screen, BLACK, center, LENGTH, FIG_LINE_WIDTH)


def draw_mark(mark, screen, center):
    if mark == "X":
        draw_x_from_center_point(screen, center)
    elif mark == "O":
        draw_o_from_center_point(screen, center)



