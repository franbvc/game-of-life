#!/usr/bin/python

import pprint
import pygame
from pygame.locals import *
import numpy as np
from organisms import std
from utils import *
from grid_patterns import *


def main():
    # Initialise screen
    pygame.init()
    screen_shape = (600, 600)
    screen = pygame.display.set_mode(screen_shape)
    pygame.display.set_caption("Basic Pygame program")
    clock = pygame.time.Clock()
    FPS = 2

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    # Display some text
    # font = pygame.font.Font(None, 36)
    # text = font.render("Hello There", 1, (10, 10, 10))
    # textpos = text.get_rect()
    # textpos.centerx = background.get_rect().centerx
    # background.blit(text, textpos)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    grid_shape = (40, 40)

    square_size, cell_screen_pos = cell_screen_position(screen_shape, grid_shape, 0.1)

    cell_grid = np.ndarray(shape=grid_shape, dtype=std.org)
    for row in range(cell_grid.shape[0]):
        for col in range(cell_grid.shape[1]):
            cell_grid[row][col] = std.org((row, col), cell_grid.shape, False)

    mosaic(cell_grid)

    # cell_grid[10][10].alive = True
    # cell_grid[11][10].alive = True
    # cell_grid[12][10].alive = True

    cell_grid[12][5].alive = True
    cell_grid[12][6].alive = True
    cell_grid[12][7].alive = True

    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        background.fill((250, 250, 250))

        draw_cells(
            cell_grid,
            (0, 0, 0),
            (250, 250, 250),
            background,
            cell_screen_pos,
            square_size,
        )

        future_state = np.ndarray(grid_shape, dtype=bool)

        for row in range(grid_shape[0]):
            for col in range(grid_shape[1]):
                future_state[row][col] = cell_grid[row][col].future_state(
                    cell_grid, False
                )

        for row in range(grid_shape[0]):
            for col in range(grid_shape[1]):
                cell_grid[row][col].alive = future_state[row][col]

        screen.blit(background, (0, 0))
        clock.tick(FPS)
        pygame.display.flip()


if __name__ == "__main__":
    main()
