from pprint import pprint


def load_grid(path):
    array_2d = []
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            row = [1 if ch == "@" else 0 for ch in line]
            array_2d.append(row)
    return array_2d


# 8 neighbor directions
DIRS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def update_grid_once(grid):
    """
    Applies one iteration of the update rule:
    - If a cell is 1 and has <4 neighbors → becomes 'X'

    Returns:
        new_grid, num_changes
    """
    rows, cols = len(grid), len(grid[0])
    result = [row[:] for row in grid]  # deep copy
    changes = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:  # only live @ cells
                neighbors = 0

                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == 1:
                            neighbors += 1

                if neighbors < 4:
                    result[r][c] = "X"
                    changes += 1

    return result, changes


def run_until_stable(grid):
    """
    Runs update_grid_once repeatedly until no changes occur.
    """
    iteration = 0
    total_changes = 0

    while True:
        iteration += 1
        grid, changes = update_grid_once(grid)
        total_changes += changes
        print(f"Iteration {iteration}: {changes} changes")

        if changes == 0:
            break

    return grid, total_changes


# ---- RUN ----
grid = load_grid("input.txt")
print("Initial grid:")
pprint(grid)

final_grid, total = run_until_stable(grid)

print("\nFinal stable grid:")
pprint(final_grid)
print("\nTotal changed over all iterations:", total)
