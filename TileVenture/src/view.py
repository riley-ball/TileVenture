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

        # Load character models:
        # 00 - 08 : Up

        # 09 - 17 : Left

        # 18 - 26 : Down

        # 27 - 35 : Right
        self.right0 = tk.PhotoImage(file="TileVenture/images/spritesheet/character/character_27.png")
        self.right1 = tk.PhotoImage(file="TileVenture/images/spritesheet/character/character_28.png")
        self.right2 = tk.PhotoImage(file="TileVenture/images/spritesheet/character/character_29.png")
        self.right3 = tk.PhotoImage(file="TileVenture/images/spritesheet/character/character_30.png")
        self.right4 = tk.PhotoImage(file="TileVenture/images/spritesheet/character/character_31.png")
        self.right5 = tk.PhotoImage(file="TileVenture/images/spritesheet/character/character_32.png")
        self.right6 = tk.PhotoImage(file="TileVenture/images/spritesheet/character/character_33.png")
        self.right7 = tk.PhotoImage(file="TileVenture/images/spritesheet/character/character_34.png")
        self.right8 = tk.PhotoImage(file="TileVenture/images/spritesheet/character/character_35.png")

        # Frames
        self.up = 0
        self.down = 0
        self.left = 0
        self.right = 0

        self.map = {}

        self.width, self.height = width, height = tuple(i * self.cell_size
                                                        for i in self.size)

        tk.Canvas.__init__(self, master, *args, width=width, height=height,
                           highlightthickness=0, **kwargs)
        self.translator = GridCoordinateTranslator()
    
    def get_map(self):
        return self.map

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
    
    def generate_map(self):
        # L: 1
        width = GRID_SIZE[0] + 500
        height = GRID_SIZE[1] + 500
        for x in range(width):
            for y in range(height):
                # top left
                if x == 0 and y == 0:
                    # self.create_image(OFFSET + x * 32, OFFSET + y * 32, image= self.photo000, tag='Terrain')
                    self.map[(x, y)] = self.photo000

                # top right
                elif x == width-1 and y == 0:
                    # self.create_image(OFFSET + x * 32, OFFSET + y * 32, image= self.photo002, tag='Terrain')
                    self.map[(x, y)] = self.photo002

                # bottom left
                elif x == 0 and y == height-1:
                    # self.create_image(OFFSET + x * 32, OFFSET + y * 32, image= self.photo046, tag='Terrain')
                    self.map[(x, y)] = self.photo046

                # bottom right
                elif x == width-1 and y == height-1:
                    # self.create_image(OFFSET + x * 32, OFFSET + y * 32, image= self.photo048, tag='Terrain')
                    self.map[(x, y)] = self.photo048
                
                # top border

                elif y == 0:
                    # self.create_image(OFFSET + x * 32, OFFSET + y * 32, image= self.photo001, tag='Terrain')
                    self.map[(x, y)] = self.photo001

                # bottom border
                elif y == height-1:
                    # self.create_image(OFFSET + x * 32, OFFSET + y * 32, image= self.photo047, tag='Terrain')
                    self.map[(x, y)] = self.photo047

                # left border
                elif x == 0:
                    # self.create_image(OFFSET + x * 32, OFFSET + y * 32, image= self.photo023, tag='Terrain')
                    self.map[(x, y)] = self.photo023

                # right border
                elif x == width-1:
                    # self.create_image(OFFSET + x * 32, OFFSET + y * 32, image= self.photo025, tag='Terrain')
                    self.map[(x, y)] = self.photo025

                # middle
                else:
                    # self.create_image(OFFSET + x * 32, OFFSET + y * 32, image= self.photo024, tag='Terrain')
                    self.map[(x, y)] = self.photo024

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
        self.delete('Terrain')
        
        gridx = grid[0]
        gridy = grid[1]

        # Frames

        # Draws from top left to bottom right
        for x in range(30):
            for y in range(18):
                self.create_image(OFFSET + x * 32, OFFSET + y * 32, image= self.map[(x + gridx - 14, y + gridy - 8)], tag='Terrain')
    
    def update_frames(self, direction):
        if direction == "Up":
            self.up += 1
            self.down = 0
            self.left = 0
            self.right = 0
        elif direction == "Down":
            self.down += 1
            self.up = 0
            self.left = 0
            self.right = 0
        elif direction == "Left":
            self.left += 1
            self.up = 0
            self.down = 0
            self.right = 0
        elif direction == "Right":
            self.right = (self.right + 1) % 9
            self.up = 0
            self.left = 0
            self.down = 0
    
    def draw_player(self, direction):
        """
        Draws player onto canvas.
        :param grid: Grid coordinates (0, 0) --> (14, 8).
        :param direction: Direction player model is facing (Up, Down, Left, Right).
        """
        self.delete('Player')

        centrex = OFFSET+14*32
        centrey = OFFSET+8*32

        if direction == 'Right':
            if self.right == 0:
                self.create_image(centrex, centrey, image=self.right0, tag='Player')
            elif self.right == 1:
                self.create_image(centrex, centrey, image=self.right1, tag='Player')
            elif self.right == 2:
                self.create_image(centrex, centrey, image=self.right2, tag='Player')
            elif self.right == 3:
                self.create_image(centrex, centrey, image=self.right3, tag='Player')
            elif self.right == 4:
                self.create_image(centrex, centrey, image=self.right4, tag='Player')
            elif self.right == 5:
                self.create_image(centrex, centrey, image=self.right5, tag='Player')
            elif self.right == 6:
                self.create_image(centrex, centrey, image=self.right6, tag='Player')
            elif self.right == 7:
                self.create_image(centrex, centrey, image=self.right7, tag='Player')
            elif self.right == 8:
                self.create_image(centrex, centrey, image=self.right8, tag='Player')
        elif direction == 'Down':
            self.create_image(centrex, centrey, image=self.photo1, tag='Player')
        elif direction == 'Left':
            self.create_image(centrex, centrey, image=self.photo2, tag='Player')
        else:
            self.create_image(centrex, centrey, image=self.photo3, tag='Player')

    def draw_level(self, level):
        """
        Draws all obstacles in level onto canvas.
        :param level: Current level player is on.
        """
        pass
