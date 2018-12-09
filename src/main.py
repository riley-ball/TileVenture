import tkinter as tk

from model import GameModel, MAP_SIZE, START_POS
from view import GameView


class Player(object):
    def __init__(self):
        pass


class GameApp(object):
    def __init__(self, master):

        self._master = master
        master.title('Game')

        self._game = game = GameModel()

        canvas_frame = tk.Canvas(master)
        canvas_frame.pack(side=tk.LEFT)

        self._view = view = GameView(canvas_frame, size=game.grid.cells,
                                     cell_size=game.grid.cell_size,
                                     bg='#1F1F1F')
        view.pack()

        self._setup_game()
        self.refresh_view(True)

        view.bind_all("<Key>", self._key_press)
        # view.bind("<Down>", self._move_down)
        # view.bind("<Left>", self._move_left)
        # view.bind("<Right>", self._move_right)

    def _setup_game(self):
        self._view.generate_map()
        self._player_grid_pos = START_POS
        self._player_direction = 'Down'

    def refresh_view(self, draw_flag, adjust_flag=0):
        self._view.draw_terrain(self._player_grid_pos, draw_flag, adjust_flag)
        self._view.draw_player(self._player_grid_pos,
                               self._player_direction, draw_flag, adjust_flag)

    def _key_press(self, event):
        key = event.keysym

        if key == "Up":
            new_coords = (self._player_grid_pos[0], self._player_grid_pos[1]-1)
            check_coords = (
                self._player_grid_pos[0], self._player_grid_pos[1]-9)
            if self._player_grid_pos[1]-1 >= 0:
                draw_flag = False
                self._player_grid_pos = new_coords
                self._player_direction = 'Up'
                self._view.update_frames(self._player_direction)
                if check_coords in self._view.get_map() and not self._view.out_of_bounds(new_coords):
                    draw_flag = True
                self.refresh_view(draw_flag)

        elif key == "Down":
            new_coords = (self._player_grid_pos[0], self._player_grid_pos[1]+1)
            check_coords = (
                self._player_grid_pos[0], self._player_grid_pos[1]+10)
            if self._player_grid_pos[1]+1 <= MAP_SIZE:
                draw_flag = False
                self._player_grid_pos = new_coords
                self._player_direction = 'Down'
                self._view.update_frames(self._player_direction)
                if check_coords in self._view.get_map() and not self._view.out_of_bounds(new_coords):
                    draw_flag = True
                self.refresh_view(draw_flag)

        elif key == "Left":
            new_coords = (self._player_grid_pos[0]-1, self._player_grid_pos[1])
            check_coords = (
                self._player_grid_pos[0]-15, self._player_grid_pos[1])
            if self._player_grid_pos[0]-1 >= 0:
                draw_flag = False
                self._player_grid_pos = new_coords
                self._player_direction = 'Left'
                self._view.update_frames(self._player_direction)
                if check_coords in self._view.get_map() and not self._view.out_of_bounds(new_coords):
                    draw_flag = True
                elif self._view.out_of_bounds(new_coords) and new_coords[0] > 14 and new_coords[0] < MAP_SIZE - 15:
                    self.refresh_view(draw_flag, 1)
                else:
                    self.refresh_view(draw_flag)

        elif key == "Right":
            x = self._player_grid_pos[0]
            y = self._player_grid_pos[1]
            new_coords = (x+1, y)
            check_coords = (
                x+16, y)
            if x+1 < MAP_SIZE:
                draw_flag = False
                self._player_grid_pos = new_coords
                self._player_direction = 'Right'
                self._view.update_frames(self._player_direction)
                if check_coords in self._view.get_map() and not self._view.out_of_bounds(new_coords):
                    draw_flag = True
                    self.refresh_view(draw_flag)
                elif self._view.out_of_bounds(new_coords) and new_coords[0] > 14 and new_coords[0] < MAP_SIZE - 15:
                    self.refresh_view(draw_flag, 1)
                else:
                    self.refresh_view(draw_flag)


def main():
    root = tk.Tk()
    root.geometry("960x576")
    game = GameApp(root)
    root.lift()
    root.attributes('-topmost', True)
    root.after_idle(root.attributes, '-topmost', False)
    root.mainloop()


if __name__ == '__main__':
    main()
