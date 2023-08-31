#!/usr/bin/python3
""" Island Perimeter."""


def island_perimeter(grid):
    """
    Island perimeter.

    Args:
        grid.
    Returns:
        Returns int, the number of the perimeter.
    """
    if not grid:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0
    
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4
                
                
                # Check neighbors (up, down, left, right) and subtract 1 for each adjacent land cell
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 1
                if row < rows - 1 and grid[row + 1][col] == 1:
                    perimeter -= 1
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 1
                if col < cols - 1 and grid[row][col + 1] == 1:
                    perimeter -= 1
                    
                    
    return perimeter
