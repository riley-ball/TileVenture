import tkinter as tk
from PIL import Image

from model import GridCoordinateTranslator, GRID_SIZE

OFFSET = 16


class GameView(tk.Canvas):
    def __init__(self, master, *args, size, cell_size, **kwargs):

        self.master = master

        self.size = size
        self.cell_size = cell_size
        self.photo = tk.PhotoImage(file="TileVenture/images/spritesheet/character/character_27.png")
        self.photo1 = tk.PhotoImage(file="TileVenture/images/spritesheet/character/character_19.png")
        self.photo2 = tk.PhotoImage(file="TileVenture/images/spritesheet/character/character_09.png")
        self.photo3 = tk.PhotoImage(file="TileVenture/images/spritesheet/character/character_01.png")
        self.photo000 = tk.PhotoImage(file="TileVenture/images/spritesheet/terrain/terrain_000.png")
        self.photo001 = tk.PhotoImage(file="TileVenture/images/spritesheet/terrain/terrain_001.png")
        self.photo002 = tk.PhotoImage(file="TileVenture/images/spritesheet/terrain/terrain_002.png")
        self.photo023 = tk.PhotoImage(file="TileVenture/images/spritesheet/terrain/terrain_023.png")
        self.photo024 = tk.PhotoImage(file="TileVenture/images/spritesheet/terrain/terrain_024.png")
        self.photo025 = tk.PhotoImage(file="TileVenture/images/spritesheet/terrain/terrain_025.png")
        self.photo046 = tk.PhotoImage(file="TileVenture/images/spritesheet/terrain/terrain_046.png")
        self.photo047 = tk.PhotoImage(file="TileVenture/images/spritesheet/terrain/terrain_047.png")
        self.photo048 = tk.PhotoImage(file="TileVenture/images/spritesheet/terrain/terrain_048.png")

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
        self.create_rectangle(0.5+grid_pos[0], 0.5+grid_pos[1], grid_pos[0]+58.5, grid_pos[1]+58.5)
    
    def draw_grass(self):
        # L: 1
        for x in range(GRID_SIZE[0]):
            for y in range(GRID_SIZE[1]):
                # top left
                if x == 0 and y == 0:
                    self.create_image(OFFSET + x * 32, OFFSET + y * 32, image= self.photo000, tag='Terrain')
                
                # top right
                elif x == GRID_SIZE[0]-1 and y == 0:
                    self.create_image(OFFSET + x * 32, OFFSET + y * 32, image= self.photo002, tag='Terrain')

                # bottom left
                elif x == 0 and y == GRID_SIZE[1]-1:
                    self.create_image(OFFSET + x * 32, OFFSET + y * 32, image= self.photo046, tag='Terrain')

                # bottom right
                elif x == GRID_SIZE[0]-1 and y == GRID_SIZE[1]-1:
                    self.create_image(OFFSET + x * 32, OFFSET + y * 32, image= self.photo048, tag='Terrain')
                
                # top border

                elif y == 0:
                    self.create_image(OFFSET + x * 32, OFFSET + y * 32, image= self.photo001, tag='Terrain')

                # bottom border
                elif y == GRID_SIZE[1]-1:
                    self.create_image(OFFSET + x * 32, OFFSET + y * 32, image= self.photo047, tag='Terrain')

                # left border
                elif x == 0:
                    self.create_image(OFFSET + x * 32, OFFSET + y * 32, image= self.photo023, tag='Terrain')

                # right border
                elif x == GRID_SIZE[0]-1:
                    self.create_image(OFFSET + x * 32, OFFSET + y * 32, image= self.photo025, tag='Terrain')

                # middle
                else:
                    self.create_image(OFFSET + x * 32, OFFSET + y * 32, image= self.photo024, tag='Terrain')

        # self.create_image(16, 16, image= self.photo000, tag='Terrain')
        # self.create_image(48, 16, image= self.photo001, tag='Terrain')
        # self.create_image(80, 16, image= self.photo002, tag='Terrain')

        # # L: 2
        # self.create_image(16, 48, image= self.photo023, tag='Terrain')
        # self.create_image(48, 48, image= self.photo024, tag='Terrain')
        # self.create_image(80, 48, image= self.photo025, tag='Terrain')

        # # L: 3
        # self.create_image(16, 80, image= self.photo046, tag='Terrain')
        # self.create_image(48, 80, image= self.photo047, tag='Terrain')
        # self.create_image(80, 80, image= self.photo048, tag='Terrain')

    def draw_terrain(self, grid):
        pass
 
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
