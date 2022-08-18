#!/usr/bin/env python3

import numpy as np
import pygame


def row_col_pos(
    grid_shape: tuple[int, int],
    margin_size: tuple[float, float],
    square_size: tuple[float, float],
) -> tuple[list[float], list[float]]:

    row_pos = []
    current_width = 0
    for row in range(grid_shape[0]):
        row_pos.append(current_width + margin_size[0])
        current_width += margin_size[0] + square_size[0]

    col_pos = []
    current_height = 0
    for col in range(grid_shape[1]):
        col_pos.append(current_height + margin_size[1])
        current_height += margin_size[1] + square_size[1]

    return (row_pos, col_pos)


def combine_row_col(
    row_pos: list[float], col_pos: list[float], grid_shape: tuple[int, int]
) -> np.ndarray:
    cell_pos_mat = np.ndarray(grid_shape, dtype=tuple)

    for idrow, row in enumerate(row_pos):
        for idcol, col in enumerate(col_pos):
            cell_pos_mat[idrow][idcol] = (row, col)

    return cell_pos_mat


def cell_screen_position(
    screen_shape: tuple[int, int], grid_shape: tuple[int, int], margin: float
) -> list[tuple[int, int], np.ndarray]:
    height_after_margin = screen_shape[0] - (screen_shape[0] * margin)
    width_after_margin = screen_shape[1] - (screen_shape[1] * margin)

    margin_size = (
        (screen_shape[0] * margin) / (grid_shape[0] + 1),
        (screen_shape[1] * margin) / (grid_shape[1] + 1),
    )

    square_size = (
        height_after_margin / grid_shape[0],
        width_after_margin / grid_shape[1],
    )

    row_pos, col_pos = row_col_pos(grid_shape, margin_size, square_size)
    cell_screen_pos = combine_row_col(row_pos, col_pos, grid_shape)

    return square_size, cell_screen_pos


def draw_cells(
    cell_grid: np.ndarray,
    live_color,
    dead_color,
    background,
    cell_screen_pos,
    square_size,
):
    grid_shape = cell_grid.shape
    for row in range(grid_shape[0]):
        for col in range(grid_shape[1]):
            cell_rect = pygame.Rect(
                cell_screen_pos[row][col][1],
                cell_screen_pos[row][col][0],
                square_size[1],
                square_size[0],
            )

            color = (0, 0, 0)
            if cell_grid[row][col].isAlive() == False:
                color = (250, 250, 250)
            pygame.draw.rect(background, color, cell_rect)

    return None


def update_cell_grid(cell_grid: np.ndarray):
    grid_shape = cell_grid.shape
    future_state = np.ndarray(grid_shape, dtype=bool)

    print(cell_grid)

    for row in range(grid_shape[0]):
        for col in range(grid_shape[1]):
            future_state[row][col] = cell_grid[row][col].future_state(cell_grid)

    for row in range(grid_shape[0]):
        for col in range(grid_shape[1]):
            cell_grid[row][col].alive = future_state[row][col]

    return cell_grid
