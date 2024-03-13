import numpy as np

class GameOfLife:
    def __init__(self, width=100, height=100):
        self.width = width
        self.height = height
        self.grid = np.zeros((height, width), dtype=bool)

    def update(self):
        new_grid = self.grid.copy()
        for row in range(self.height):
            for col in range(self.width):
                live_neighbors = self._count_live_neighbors(row, col)
                if self.grid[row, col]:  # Cell is alive
                    if live_neighbors < 2 or live_neighbors > 3:
                        new_grid[row, col] = False
                else:  # Cell is dead
                    if live_neighbors == 3:
                        new_grid[row, col] = True
        self.grid = new_grid

    def _count_live_neighbors(self, row, col):
        count = int((self.grid[max(0, row-1):min(self.height, row+2),
                               max(0, col-1):min(self.width, col+2)]).sum())
        count -= self.grid[row, col]
        return count

    def reset(self):
        self.grid = np.zeros((self.height, self.width), dtype=bool)
