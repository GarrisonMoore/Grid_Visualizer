import os
import random
import time


def count_neighbors(grid, r, c):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            neighbor_r = r + i
            neighbor_c = c + j

            if 0 <= neighbor_r < len(grid) and 0 <= neighbor_c < len(grid[0]):
                count += grid[neighbor_r][neighbor_c]
    return count


def update_grid(old_grid):
    rows = len(old_grid)
    columns = len(old_grid[0])

    new_grid = []
    for i in range(rows):
        new_grid.append([0] * columns)

    for r in range(rows):
        for c in range(columns):
            neighbors = count_neighbors(old_grid, r, c)
            current_state = old_grid[r][c]

            # Rule 1: Survival
            if current_state == 1 and (neighbors == 2 or neighbors == 3):
                new_grid[r][c] = 1

            # Rule 2: Birth
            elif current_state == 0 and neighbors == 3:
                new_grid[r][c] = 1

    return new_grid


if __name__ == "__main__":
    # Expand the grid size for a better visual field
    rows = 15
    columns = 20
    grid = []

    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(random.randint(0, 1))
        grid.append(row)

    while True:
        # Clear the terminal for rendering
        os.system('clear')

        # Render the grid using blocks for visibility
        for row in grid:
            print(" ".join("█" if cell == 1 else "." for cell in row))

        grid = update_grid(grid)
        time.sleep(0.1)