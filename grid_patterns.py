#!/usr/bin/env python3

import numpy as np
import pygame


def kickback_180_degree(cell_grid: np.ndarray):
    cell_grid[5][5].alive = True
    cell_grid[6][4].alive = True
    cell_grid[7][4].alive = True
    cell_grid[7][5].alive = True
    cell_grid[7][6].alive = True

    cell_grid[10][5].alive = True
    cell_grid[10][6].alive = True
    cell_grid[11][4].alive = True
    cell_grid[11][6].alive = True
    cell_grid[12][6].alive = True

    return None


def mosaic(cell_grid: np.ndarray):
    cell_grid[4][4].alive = True
    cell_grid[4][6].alive = True
    cell_grid[5][5].alive = True
    cell_grid[7][4].alive = True
    cell_grid[7][5].alive = True
    cell_grid[7][6].alive = True

    return None
