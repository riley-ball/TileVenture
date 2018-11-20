import tkinter as tk
from model import GridCoordinateTranslator

class GameView(tk.Canvas):
    def __init__(self, master, *args, size=(6, 6), cell_size=40, **kwargs):

        self.master = master

        self.size = size
        self.cell_size = cell_size
        self.photo = tk.PhotoImage(file="Right.gif")
        self.photo1 = tk.PhotoImage(file="Down.gif")
        self.photo2 = tk.PhotoImage(file="Left.gif")
        self.photo3 = tk.PhotoImage(file="Up.gif")

        self.width, self.height = width, height = tuple(i * self.cell_size
                                                        for i in self.size)

        tk.Canvas.__init__(self, master, *args, width=width, height=height,
                           highlightthickness=0, **kwargs)
        self.translator = GridCoordinateTranslator()

    def draw_borders(self, borders, fill='goldenrod'):
        """
        Draws the border lines of the game view, after first removing any existing

        Parameters:
            borders (iter<tuple<int, int>,
                          tuple<int, int>>): A series of pixel positions for
                                             laying out the borders of the view.
            fill (str): The colour of the borders to draw
        """
        self.delete('border')
        for start, end in borders:
            self.create_line(start, end, fill=fill, tag='border')

    def draw_tiles(self, grid):
        grid_pos = self.translator.grid_to_coords_corner(grid)
        self.create_rectangle(0.5+grid_pos[0], 0.5+grid_pos[1], grid_pos[0]+58.5, grid_pos[1]+58.5, fill='aqua')

    def draw_player(self, grid, direction):
        """
        Draws player onto canvas.
        :param grid: Grid coordinates (0, 0) --> (14, 8).
        :param direction: Direction player model is facing (Up, Down, Left, Right).
        """
        self.delete('Player')
        grid_pos = self.translator.grid_to_coords_corner(grid)
        if direction == 'Right':
            self.create_image(30+grid_pos[0], 30+grid_pos[1], image=self.photo, tag='Player')
        elif direction == 'Down':
            self.create_image(30+grid_pos[0], 30+grid_pos[1], image=self.photo1, tag='Player')
        elif direction == 'Left':
            self.create_image(30+grid_pos[0], 30+grid_pos[1], image=self.photo2, tag='Player')
        else:
            self.create_image(30+grid_pos[0], 30+grid_pos[1], image=self.photo3, tag='Player')

    def draw_level(self, level):
        """
        Draws all obstacles in level onto canvas.
        :param level: Current level player is on.
        """
        pass
