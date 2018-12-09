import tkinter as tk
from PIL import Image

from model import GridCoordinateTranslator, GRID_SIZE, MAP_SIZE

OFFSET = 16

class GameView(tk.Canvas):
    def __init__(self, master, *args, size, cell_size, **kwargs):

        self.master = master

        self.size = size
        self.cell_size = cell_size
        self.photo000 = tk.PhotoImage(file="images/terrain/terrain_000.png")
        self.photo001 = tk.PhotoImage(file="images/terrain/terrain_001.png")
        self.photo002 = tk.PhotoImage(file="images/terrain/terrain_002.png")
        self.photo023 = tk.PhotoImage(file="images/terrain/terrain_023.png")
        self.photo024 = tk.PhotoImage(file="images/terrain/terrain_024.png")
        self.photo025 = tk.PhotoImage(file="images/terrain/terrain_025.png")
        self.photo046 = tk.PhotoImage(file="images/terrain/terrain_046.png")
        self.photo047 = tk.PhotoImage(file="images/terrain/terrain_047.png")
        self.photo048 = tk.PhotoImage(file="images/terrain/terrain_048.png")

        # Load character models:
        # 00 - 08 : Up
        self.up_frame = [tk.PhotoImage(file="images/character/character_00.png"),
        tk.PhotoImage(file="images/character/character_01.png"), 
        tk.PhotoImage(file="images/character/character_02.png"), 
        tk.PhotoImage(file="images/character/character_03.png"), 
        tk.PhotoImage(file="images/character/character_04.png"), 
        tk.PhotoImage(file="images/character/character_05.png"), 
        tk.PhotoImage(file="images/character/character_06.png"), 
        tk.PhotoImage(file="images/character/character_07.png"), 
        tk.PhotoImage(file="images/character/character_08.png")]

        # 09 - 17 : Left
        self.left_frame = [tk.PhotoImage(file="images/character/character_09.png"),
        tk.PhotoImage(file="images/character/character_10.png"),
        tk.PhotoImage(file="images/character/character_11.png"),
        tk.PhotoImage(file="images/character/character_12.png"),
        tk.PhotoImage(file="images/character/character_13.png"),
        tk.PhotoImage(file="images/character/character_14.png"),
        tk.PhotoImage(file="images/character/character_15.png"),
        tk.PhotoImage(file="images/character/character_16.png"),
        tk.PhotoImage(file="images/character/character_17.png")]

        # 18 - 26 : Down
        self.down_frame = [tk.PhotoImage(file="images/character/character_18.png"),
        tk.PhotoImage(file="images/character/character_19.png"),
        tk.PhotoImage(file="images/character/character_20.png"),
        tk.PhotoImage(file="images/character/character_21.png"),
        tk.PhotoImage(file="images/character/character_22.png"),
        tk.PhotoImage(file="images/character/character_23.png"),
        tk.PhotoImage(file="images/character/character_24.png"),
        tk.PhotoImage(file="images/character/character_25.png"),
        tk.PhotoImage(file="images/character/character_26.png")]

        # 27 - 35 : Right
        self.right_frame = [tk.PhotoImage(file="images/character/character_27.png"),
        tk.PhotoImage(file="images/character/character_28.png"),
        tk.PhotoImage(file="images/character/character_29.png"),
        tk.PhotoImage(file="images/character/character_30.png"),
        tk.PhotoImage(file="images/character/character_31.png"),
        tk.PhotoImage(file="images/character/character_32.png"),
        tk.PhotoImage(file="images/character/character_33.png"),
        tk.PhotoImage(file="images/character/character_34.png"),
        tk.PhotoImage(file="images/character/character_35.png")]

        # Misc
        self.lake0 = tk.PhotoImage(file="images/terrain/terrain_416.png")
        self.lake1 = tk.PhotoImage(file="images/terrain/terrain_417.png")
        self.lake2 = tk.PhotoImage(file="images/terrain/terrain_418.png")
        self.lake3 = tk.PhotoImage(file="images/terrain/terrain_436.png")
        self.lake4 = tk.PhotoImage(file="images/terrain/terrain_392.png")
        self.lake5 = tk.PhotoImage(file="images/terrain/terrain_435.png")
        self.lake6 = tk.PhotoImage(file="images/terrain/terrain_437.png")
        self.lake7 = tk.PhotoImage(file="images/terrain/terrain_438.png")
        self.lake8 = tk.PhotoImage(file="images/terrain/terrain_439.png")

        self.misc0 = tk.PhotoImage(file="images/terrain/terrain_159.png")

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

    def generate_map(self):
        # L: 1
        width = MAP_SIZE
        height = MAP_SIZE
        count = 0
        for x in range(width):
            for y in range(height):
                # top left
                if x == 0 and y == 0:
                    self.map[(x, y)] = self.photo000, 

                # top right
                elif x == width-1 and y == 0:
                    self.map[(x, y)] = self.photo002, 

                # bottom left
                elif x == 0 and y == height-1:
                    self.map[(x, y)] = self.photo046, 

                # bottom right
                elif x == width-1 and y == height-1:
                    self.map[(x, y)] = self.photo048, 
                
                # top border

                elif y == 0:
                    self.map[(x, y)] = self.photo001, 

                # bottom border
                elif y == height-1:
                    self.map[(x, y)] = self.photo047, 

                # left border
                elif x == 0:
                    self.map[(x, y)] = self.photo023, 

                # right border
                elif x == width-1:
                    self.map[(x, y)] = self.photo025, 

                # small lake
                elif (x >= 26 and x <= 28) and (y >= 14 and y <= 16):
                    if x == 26 and y == 14:
                        self.map[(x, y)] = self.lake0, 
                    elif x == 27 and y == 14:
                        self.map[(x, y)] = self.lake1, 
                    elif x == 28 and y == 14:
                        self.map[(x, y)] = self.lake2, 
                    elif x == 26 and y == 15:
                        self.map[(x, y)] = self.lake3, 
                    elif x == 27 and y == 15:
                        self.map[(x, y)] = self.lake4, 
                    elif x == 28 and y == 15:
                        self.map[(x, y)] = self.lake5, 
                    elif x == 26 and y == 16:
                        self.map[(x, y)] = self.lake6, 
                    elif x == 27 and y == 16:
                        self.map[(x, y)] = self.lake7, 
                    elif x == 28 and y == 16:
                        self.map[(x, y)] = self.lake8, 

                # middle
                else:
                    self.map[(x, y)] = self.photo024, 
                    if y == 4 and count % 15 == 0:
                        self.map[(x, y)] = self.photo024, self.misc0
                    count += 1

    def draw_terrain(self, grid):
        self.delete('Terrain')
        
        # Player grid positions
        gridx = grid[0]
        gridy = grid[1]

        # Draws from top left to bottom right
        for x in range(30):
            for y in range(18):
                # position in view
                xcoord = OFFSET + x * 32
                ycoord = OFFSET + y * 32

                # positin in map dict
                xmap = x + gridx - 14
                ymap = y + gridy - 8

                if len(self.map[(x + gridx - 14, y + gridy - 8)]) == 1:
                    self.create_image(xcoord, ycoord, image= self.map[(xmap, ymap)][0], tag='Terrain')
                else:
                    self.create_image(xcoord, ycoord, image= self.map[(xmap, ymap)][0], tag='Terrain')
                    self.create_image(xcoord, ycoord, image= self.map[(xmap, ymap)][1], tag='Terrain')
    
    def update_frames(self, direction):
        if direction == "Up":
            self.up = (self.up + 1) % 9
            self.down = 0
            self.left = 0
            self.right = 0
        elif direction == "Down":
            self.down = (self.down + 1) % 9
            self.up = 0
            self.left = 0
            self.right = 0
        elif direction == "Left":
            self.left = (self.left + 1) % 9
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
            self.create_image(centrex, centrey, image=self.right_frame[self.right], tag='Player')
        elif direction == 'Down':
            self.create_image(centrex, centrey, image=self.down_frame[self.down], tag='Player')
        elif direction == 'Left':
            self.create_image(centrex, centrey, image=self.left_frame[self.left], tag='Player')
        else:
            self.create_image(centrex, centrey, image=self.up_frame[self.up], tag='Player')
