import os
import random
import time

def count_neighbors(grid, r, c):
    """
    Count the neighbors of a specific cell
    """
    count = 0

    # iterate through a 3x3 grid surrounding the target
    for x in range(-1, 2):
        for y in range(-1, 2):
            # skip the cell we are counting for
            if x == 0 and y == 0:
                continue

            # calculate the location of the neighbor pm the grid
            neighbor_r = r + x
            neighbor_c = c + y

            # check boundary before proceeding. Makes sure we aren't counting something off the grid
            if 0 <= neighbor_r < len(grid) and 0 <= neighbor_c < len(grid[0]):
                # add the value at that coordinate
                count += grid[neighbor_r][neighbor_c]
    return count

def update_grid(old_grid):
    """
    Applies the rules of Conways game of life to generate the next grid
    """

    # match new grid to the old one
    rows = len(old_grid)
    columns = len(old_grid[0])
    new_grid = []

    # Generate a new grid
    for i in range(rows):
        new_grid.append([0] * columns)

    # iterate through rows and columns
    for r in range(rows):
        for c in range(columns):
            # count neighbors of each cell
            neighbors = count_neighbors(old_grid, r, c)
            # determine whether the current cell is dead or alive
            current_state = old_grid[r][c]

            # Rule 1: Survival
            # If the cell is alive and has 2 or 3 neighbors
            if current_state == 1 and (neighbors == 2 or neighbors == 3):
                # set the cell to live (1)
                new_grid[r][c] = 1

            # Rule 2: Birth
            # if the cell is dead and has 3 neighbors
            elif current_state == 0 and neighbors == 3:
                # cell comes alive (1)
                new_grid[r][c] = 1

    return new_grid


if __name__ == "__main__":
    """
    Run the shit
    """
    # define rows and columns
    rows = 30
    columns = 30
    grid = []

    # create the grid
    for i in range(rows):
        row = []
        for j in range(columns):
            # append random binary values to the rows
            row.append(random.randint(0, 1))
        # append the generated grid to the rows
        grid.append(row)

    # render the grid
    while True:
        # clear the terminal for rendering
        os.system('cls' if os.name == 'nt' else 'clear')

        # Render the grid using blocks for visibility
        for row in grid:
            print(" ".join("█" if cell == 1 else "." for cell in row))

        grid = update_grid(grid)
        time.sleep(0.1)