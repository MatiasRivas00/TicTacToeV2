import pygame
import math
import cmath


def new_cord(x, y):
    i = x//200
    j = y//200
    return int(i), int(j)


def fig_center(i, j):
    p_x = i*200 + 100
    p_y = j*200 + 100
    return p_x, p_y

