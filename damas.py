
import pygame as pg

from pygame.locals import (
    MOUSEBUTTONUP,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pg.init()
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
running = True

tela = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


class BoardSquare:
    def __init__(self, x_start, y_start, width_height, is_white):
        self.x_start = x_start
        self.y_start = y_start
        self.width_height = width_height
        self.is_white = is_white


def calculate_coordinates(x_array, y_array, is_white):
    if SCREEN_WIDTH < SCREEN_HEIGHT or SCREEN_WIDTH == SCREEN_HEIGHT:
        width_height = SCREEN_WIDTH / 8
    else:
        width_height = SCREEN_HEIGHT / 8

    x_coordinate = x_array * width_height
    y_coordinate = y_array * width_height

    return BoardSquare(x_coordinate, y_coordinate, width_height, is_white)


chess_board = []
is_white = False
for y in range(8):
    chess_row = []
    is_white = not is_white
    for x in range(8):
        chess_row.append(calculate_coordinates(x, y, is_white))
        is_white = not is_white
    chess_board.append(chess_row)


for row in chess_board:
    for square in row:
        surf = pg.Surface((square.width_height, square.width_height))

        if square.is_white:
            surf.fill((255, 255, 255))
        else:
            surf.fill((0, 0, 0))

        rect = surf.get_rect()
        tela.blit(surf, (square.x_start, square.y_start))
        pg.display.flip()


pg.display.set_caption("Jogo de Damas")

while running:
    for event in pg.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        if event.type == MOUSEBUTTONUP:
            pos = pg.mouse.get_pos()
            highlight_selected_square(get_square_for_position(pos))
        elif event.type == QUIT:
            running = False


def get_square_for_position(pos):
    for row in chess_board:
        if row[0].y_start < pos[1] < row[0].y_start + row[0].width_height:
            for square in row:
                if square.x_start < pos[0] < square.x_start + square.width_height:
                    return square
