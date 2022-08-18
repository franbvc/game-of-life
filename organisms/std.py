import numpy as np
import pprint


class org:
    def __init__(self, pos: tuple[int, int], grid_shape: tuple[int, int], alive: bool):
        self.row: int = pos[0]
        self.col: int = pos[1]
        self.neighbours: list[tuple[int, int]] = self.find_neighbours(grid_shape)
        self.alive: bool = alive

    def __str__(self):
        if self.alive:
            return f"ALIVE at pos: {self.row}, {self.col}"

        return f"DEAD at pos: {self.row}, {self.col}"

    def __repr__(self):
        if self.alive:
            return "1"

        return "0"

    def isAlive(self) -> bool:
        return self.alive

    def find_neighbours(self, grid_shape) -> list[tuple[int, int]]:
        last_row: int = grid_shape[0] - 1
        last_col: int = grid_shape[1] - 1
        neighbours: list[tuple[int, int]] = []

        for row in range(-1, 2, 1):
            for col in range(-1, 2, 1):
                if row == 0 and col == 0:
                    continue
                if (self.row + row) < 0 or (self.col + col) < 0:
                    continue
                if (self.row + row) > last_row or (self.col + col) > last_col:
                    continue

                neighbours.append((self.row + row, self.col + col))

        return neighbours

    def future_state(self, grid: np.ndarray, describe: bool) -> bool:
        alive_neighbours: int = 0

        for pos in self.neighbours:
            if grid[pos[0]][pos[1]].alive == True:
                alive_neighbours += 1

        if self.alive == False:
            if alive_neighbours == 3:
                return True
            return False

        if self.alive == True:
            if alive_neighbours == 2:
                return True
            if alive_neighbours == 3:
                return True

        return False
