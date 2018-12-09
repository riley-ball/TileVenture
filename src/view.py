import tkinter as tk
from PIL import Image

from model import GridCoordinateTranslator, GRID_SIZE

OFFSET = 16


class GameView(tk.Canvas):
    def __init__(self, master, *args, size, cell_size, **kwargs):

        self.master = master

        self.size = size
        self.cell_size = cell_size
        self.photo = tk.PhotoImage(file="images/spritesheet/character/character_27.png")
        self.photo1 = tk.PhotoImage(file="images/spritesheet/character/character_19.png")
        self.photo2 = tk.PhotoImage(file="images/spritesheet/character/character_09.png")
        self.photo3 = tk.PhotoImage(file="images/spritesheet/character/character_01.png")
        self.photo000 = tk.PhotoImage(file="images/spritesheet/terrain/terrain_000.png")
        self.photo001 = tk.PhotoImage(file="images/spritesheet/terrain/terrain_001.png")
        self.photo002 = tk.PhotoImage(file="images/spritesheet/terrain/terrain_002.png")
        self.photo023 = tk.PhotoImage(file="images/spritesheet/terrain/terrain_023.png")
        self.photo024 = tk.PhotoImage(file="images/spritesheet/terrain/terrain_024.png")
        self.photo025 = tk.PhotoImage(file="images/spritesheet/terrain/terrain_025.png")
        self.photo046 = tk.PhotoImage(file="images/spritesheet/terrain/terrain_046.png")
        self.photo047 = tk.PhotoImage(file="images/spritesheet/terrain/terrain_047.png")
        self.photo048 = tk.PhotoImage(file="images/spritesheet/terrain/terrain_048.png")

        # Load character models:
        # 00 - 08 : Up
        self.up0 = tk.PhotoImage(file="images/spritesheet/character/character_00.png")
        self.up1 = tk.PhotoImage(file="images/spritesheet/character/character_01.png")
        self.up2 = tk.PhotoImage(file="images/spritesheet/character/character_02.png")
        self.up3 = tk.PhotoImage(file="images/spritesheet/character/character_03.png")
        self.up4 = tk.PhotoImage(file="images/spritesheet/character/character_04.png")
        self.up5 = tk.PhotoImage(file="images/spritesheet/character/character_05.png")
        self.up6 = tk.PhotoImage(file="images/spritesheet/character/character_06.png")
        self.up7 = tk.PhotoImage(file="images/spritesheet/character/character_07.png")
        self.up8 = tk.PhotoImage(file="images/spritesheet/character/character_08.png")

        # 09 - 17 : Left
        self.left0 = tk.PhotoImage(file="images/spritesheet/character/character_09.png")
        self.left1 = tk.PhotoImage(file="images/spritesheet/character/character_10.png")
        self.left2 = tk.PhotoImage(file="images/spritesheet/character/character_11.png")
        self.left3 = tk.PhotoImage(file="images/spritesheet/character/character_12.png")
        self.left4 = tk.PhotoImage(file="images/spritesheet/character/character_13.png")
        self.left5 = tk.PhotoImage(file="images/spritesheet/character/character_14.png")
        self.left6 = tk.PhotoImage(file="images/spritesheet/character/character_15.png")
        self.left7 = tk.PhotoImage(file="images/spritesheet/character/character_16.png")
        self.left8 = tk.PhotoImage(file="images/spritesheet/character/character_17.png")

        # 18 - 26 : Down
        self.down0 = tk.PhotoImage(file="images/spritesheet/character/character_18.png")
        self.down1 = tk.PhotoImage(file="images/spritesheet/character/character_19.png")
        self.down2 = tk.PhotoImage(file="images/spritesheet/character/character_20.png")
        self.down3 = tk.PhotoImage(file="images/spritesheet/character/character_21.png")
        self.down4 = tk.PhotoImage(file="images/spritesheet/character/character_22.png")
        self.down5 = tk.PhotoImage(file="images/spritesheet/character/character_23.png")
        self.down6 = tk.PhotoImage(file="images/spritesheet/character/character_24.png")
        self.down7 = tk.PhotoImage(file="images/spritesheet/character/character_25.png")
        self.down8 = tk.PhotoImage(file="images/spritesheet/character/character_26.png")

        # 27 - 35 : Right
        self.right0 = tk.PhotoImage(file="images/spritesheet/character/character_27.png")
        self.right1 = tk.PhotoImage(file="images/spritesheet/character/character_28.png")
        self.right2 = tk.PhotoImage(file="images/spritesheet/character/character_29.png")
        self.right3 = tk.PhotoImage(file="images/spritesheet/character/character_30.png")
        self.right4 = tk.PhotoImage(file="images/spritesheet/character/character_31.png")
        self.right5 = tk.PhotoImage(file="images/spritesheet/character/character_32.png")
        self.right6 = tk.PhotoImage(file="images/spritesheet/character/character_33.png")
        self.right7 = tk.PhotoImage(file="images/spritesheet/character/character_34.png")
        self.right8 = tk.PhotoImage(file="images/spritesheet/character/character_35.png")

        # Misc
        self.lake0 = tk.PhotoImage(file="images/spritesheet/terrain/terrain_416.png")
        self.lake1 = tk.PhotoImage(file="images/spritesheet/terrain/terrain_417.png")
        self.lake2 = tk.PhotoImage(file="images/spritesheet/terrain/terrain_418.png")
        self.lake3 = tk.PhotoImage(file="images/spritesheet/terrain/terrain_436.png")
        self.lake4 = tk.PhotoImage(file="images/spritesheet/terrain/terrain_392.png")
        self.lake5 = tk.PhotoImage(file="images/spritesheet/terrain/terrain_435.png")
        self.lake6 = tk.PhotoImage(file="images/spritesheet/terrain/terrain_437.png")
        self.lake7 = tk.PhotoImage(file="images/spritesheet/terrain/terrain_438.png")
        self.lake8 = tk.PhotoImage(file="images/spritesheet/terrain/terrain_439.png")

        self.misc0 = tk.PhotoImage(file="images/spritesheet/terrain/terrain_159.png")

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
    
    """
    EVERYTHING IN THIS FUNCTION IS HARDCODED :(
    """

    def generate_map(self):
        # L: 1
        width = GRID_SIZE[0] + 500
        height = GRID_SIZE[1] + 500
        count = 0
        for x in range(width):
            for y in range(height):
                # top left
                if x == 0 and y == 0:
                    # self.create_image(OFFSET + x * 32, OFFSET + y * 32, image= self.photo000, tag='Terrain')
                    self.map[(x, y)] = (self.photo000, )

                # top right
                elif x == width-1 and y == 0:
                    # self.create_image(OFFSET + x * 32, OFFSET + y * 32, image= self.photo002, tag='Terrain')
                    self.map[(x, y)] = (self.photo002, )

                # bottom left
                elif x == 0 and y == height-1:
                    # self.create_image(OFFSET + x * 32, OFFSET + y * 32, image= self.photo046, tag='Terrain')
                    self.map[(x, y)] = (self.photo046, )

                # bottom right
                elif x == width-1 and y == height-1:
                    # self.create_image(OFFSET + x * 32, OFFSET + y * 32, image= self.photo048, tag='Terrain')
                    self.map[(x, y)] = (self.photo048, )
                
                # top border

                elif y == 0:
                    # self.create_image(OFFSET + x * 32, OFFSET + y * 32, image= self.photo001, tag='Terrain')
                    self.map[(x, y)] = (self.photo001, )

                # bottom border
                elif y == height-1:
                    # self.create_image(OFFSET + x * 32, OFFSET + y * 32, image= self.photo047, tag='Terrain')
                    self.map[(x, y)] = (self.photo047, )

                # left border
                elif x == 0:
                    # self.create_image(OFFSET + x * 32, OFFSET + y * 32, image= self.photo023, tag='Terrain')
                    self.map[(x, y)] = (self.photo023, )

                # right border
                elif x == width-1:
                    # self.create_image(OFFSET + x * 32, OFFSET + y * 32, image= self.photo025, tag='Terrain')
                    self.map[(x, y)] = (self.photo025, )

                # small lake
                elif (x >= 26 and x <= 28) and (y >= 14 and y <= 16):
                    if x == 26 and y == 14:
                        self.map[(x, y)] = (self.lake0, )
                    elif x == 27 and y == 14:
                        self.map[(x, y)] = (self.lake1, )
                    elif x == 28 and y == 14:
                        self.map[(x, y)] = (self.lake2, )
                    elif x == 26 and y == 15:
                        self.map[(x, y)] = (self.lake3, )
                    elif x == 27 and y == 15:
                        self.map[(x, y)] = (self.lake4, )
                    elif x == 28 and y == 15:
                        self.map[(x, y)] = (self.lake5, )
                    elif x == 26 and y == 16:
                        self.map[(x, y)] = (self.lake6, )
                    elif x == 27 and y == 16:
                        self.map[(x, y)] = (self.lake7, )
                    elif x == 28 and y == 16:
                        self.map[(x, y)] = (self.lake8, )

                # middle
                else:
                    # self.create_image(OFFSET + x * 32, OFFSET + y * 32, image= self.photo024, tag='Terrain')
                    self.map[(x, y)] = (self.photo024, )
                    if y == 4 and count % 15 == 0:
                        self.map[(x, y)] = (self.photo024, self.misc0)
                    count += 1
                    

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
                if len(self.map[(x + gridx - 14, y + gridy - 8)]) == 1:
                    self.create_image(OFFSET + x * 32, OFFSET + y * 32, image= self.map[(x + gridx - 14, y + gridy - 8)][0], tag='Terrain')
                else:
                    self.create_image(OFFSET + x * 32, OFFSET + y * 32, image= self.map[(x + gridx - 14, y + gridy - 8)][0], tag='Terrain')
                    self.create_image(OFFSET + x * 32, OFFSET + y * 32, image= self.map[(x + gridx - 14, y + gridy - 8)][1], tag='Terrain')
    
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
            if self.down == 0:
                self.create_image(centrex, centrey, image=self.down0, tag='Player')
            elif self.down == 1:
                self.create_image(centrex, centrey, image=self.down1, tag='Player')
            elif self.down == 2:
                self.create_image(centrex, centrey, image=self.down2, tag='Player')
            elif self.down == 3:
                self.create_image(centrex, centrey, image=self.down3, tag='Player')
            elif self.down == 4:
                self.create_image(centrex, centrey, image=self.down4, tag='Player')
            elif self.down == 5:
                self.create_image(centrex, centrey, image=self.down5, tag='Player')
            elif self.down == 6:
                self.create_image(centrex, centrey, image=self.down6, tag='Player')
            elif self.down == 7:
                self.create_image(centrex, centrey, image=self.down7, tag='Player')
            elif self.down == 8:
                self.create_image(centrex, centrey, image=self.down8, tag='Player')
        elif direction == 'Left':
            if self.left == 0:
                self.create_image(centrex, centrey, image=self.left0, tag='Player')
            elif self.left == 1:
                self.create_image(centrex, centrey, image=self.left1, tag='Player')
            elif self.left == 2:
                self.create_image(centrex, centrey, image=self.left2, tag='Player')
            elif self.left == 3:
                self.create_image(centrex, centrey, image=self.left3, tag='Player')
            elif self.left == 4:
                self.create_image(centrex, centrey, image=self.left4, tag='Player')
            elif self.left == 5:
                self.create_image(centrex, centrey, image=self.left5, tag='Player')
            elif self.left == 6:
                self.create_image(centrex, centrey, image=self.left6, tag='Player')
            elif self.left == 7:
                self.create_image(centrex, centrey, image=self.left7, tag='Player')
            elif self.left == 8:
                self.create_image(centrex, centrey, image=self.left8, tag='Player')
        else:
            if self.up == 0:
                self.create_image(centrex, centrey, image=self.up0, tag='Player')
            elif self.up == 1:
                self.create_image(centrex, centrey, image=self.up1, tag='Player')
            elif self.up == 2:
                self.create_image(centrex, centrey, image=self.up2, tag='Player')
            elif self.up == 3:
                self.create_image(centrex, centrey, image=self.up3, tag='Player')
            elif self.up == 4:
                self.create_image(centrex, centrey, image=self.up4, tag='Player')
            elif self.up == 5:
                self.create_image(centrex, centrey, image=self.up5, tag='Player')
            elif self.up == 6:
                self.create_image(centrex, centrey, image=self.up6, tag='Player')
            elif self.up == 7:
                self.create_image(centrex, centrey, image=self.up7, tag='Player')
            elif self.up == 8:
                self.create_image(centrex, centrey, image=self.up8, tag='Player')

    def draw_level(self, level):
        """
        Draws all obstacles in level onto canvas.
        :param level: Current level player is on.
        """
        pass
