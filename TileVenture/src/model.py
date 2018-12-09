from typing import Tuple, List

CELL_SIZE = 32
PIXEL_SIZE = (24, 12)
GRID_SIZE = (30, 18)


class GridCoordinateTranslator:
    """Translates coordinates between cells in a grid (column, row) & pixels (x, y)

    Cells are treated as square
    """
    # cell is frequently used as a shorthand for cell position, as with pixel
    cells: Tuple[int, int]  # The number of (column, row) cells in the grid
    cell_size: int  # The number of pixels wide & high each cell is
    pixels: Tuple[int, int]  # The number of (x, y) pixels in the grid

    def __init__(self, cells: Tuple[int, int] = PIXEL_SIZE,
                 cell_size: int = CELL_SIZE):
        """Construct a coordinate translator

        Parameters:
            cells (tuple<int, int>): Grid dimensions
            cell_size (int): The side length of the cell
        """
        self.cells = cells
        self.cell_size = cell_size

        # convert grid dimensions to pixel dimensions
        self.pixels = tuple(i * cell_size for i in cells)

    def is_cell_valid(self, cell):
        """(bool) Returns True iff 'cell' position exists in the grid"""
        column, row = cell
        columns, rows = self.cells

        return 0 <= column < columns and 0 <= row < rows

    def is_pixel_valid(self, pixel):
        """(bool) Returns True iff 'cell' position exists in the grid

        Note, bottom-right most valid consists of coordinates that are
        length of their axis minus one. I.e. in a 600x400 grid, the
        bottom-right most valid pixel is (599, 399)."""
        x, y = pixel
        max_x, max_y = self.pixels

        return 0 <= x < max_x and 0 <= y < max_y

    def cell_to_pixel_centre(self, cell):
        """(int, int) Returns the pixel position at the centre of 'cell'"""
        return tuple(int((i + .5) * self.cell_size) for i in cell)

    def cell_to_pixel_corner(self, cell):
        """(int, int) Returns the pixel position at the top-left corner of 'cell'"""
        return tuple(i * self.cell_size for i in cell)

    def pixel_to_cell(self, pixel):
        """(int, int) Returns the position of the cell that contains the pixel position"""
        return tuple(int(i // self.cell_size) for i in pixel)

    def pixel_to_cell_offset(self, pixel):
        """(float, float) Returns the fractional offset of a pixel position
        from the centre of the corresponding cell

        A fractional offset is the proportion of the cell's length that each
        pixel coordinate is away from the pixel centre, and hence each value
        of the result will be in the range [-0.5, 0.5]

        I.e.
             Cell Offset  | Position
            -----------------------------------------------------------------------
             (-0.5, -0.5) | Top-left corner
             ( 0.5,  0.5) | Bottom-right corner
             (   0,    0) | Centre
             (-0.25, 0.4) | Half way between the centre and the left edge,
                          | & 80% of the way between the centre and the bottom edge
        """
        return tuple((i / self.cell_size) % 1 - .5 for i in pixel)

    def get_border_coordinates(self, include_outer=True):
        """
        Yields the pixel coordinates for every border

        Parameters:
            include_outer (bool): includes outermost borders if True
        """
        offset = 1 if include_outer else 0
        width, height = self.pixels

        columns, rows = self.cells

        for column in range(1 - offset, columns + offset):
            x = column * self.cell_size
            yield (x, 0), (x, height)

        for row in range(1 - offset, rows + offset):
            y = row * self.cell_size
            yield (0, y), (width, y)

    def grid_to_coords_corner(self, grid):
        """
        Takes grid position and translates to pixel position
        :param grid: Tuple of grid positions
        :return: pixel positions
        """
        return (grid[0]*60, grid[1]*60)

class GameModel(object):
    def __init__(self, size=GRID_SIZE, cell_size=CELL_SIZE):
        """Construct a new game"""
        super().__init__()

        self.grid = GridCoordinateTranslator(cells=size, cell_size=cell_size)
