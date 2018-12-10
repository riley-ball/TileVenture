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
        self.refresh_view(5)

        view.bind_all("<Key>", self._key_press)
        view.bind_all("<KeyPress>", self.keydown)
        view.bind_all("<KeyRelease>", self.keyup)
        self._key_flag = False

    def _setup_game(self):
        self._view.generate_map()
        self._player_grid_pos = START_POS
        self._player_direction = 'Down'

    def refresh_view(self, draw_flag):
        self._view.draw_terrain(self._player_grid_pos, draw_flag)
        self._view.draw_player(self._player_grid_pos,
                               self._player_direction, draw_flag)

    def keyup(self, e):
        self._key_flag = False
        print('up', e.char, e.type)

    def keydown(self, e):
        self._key_flag = True
        self._key_press(e)

    def _key_press(self, event):
        key = event.keysym
        while self._key_flag:
            if key == "Up":
                print(event.type,  "aaaaa")
                new_coords = (
                    self._player_grid_pos[0], self._player_grid_pos[1]-1)
                if self._player_grid_pos[1]-1 >= 0:
                    self._player_grid_pos = new_coords
                    self._player_direction = 'Up'
                    self._view.update_frames(self._player_direction)
                    self.refresh_view(self._view.out_of_bounds(new_coords))

            elif key == "Down":
                new_coords = (
                    self._player_grid_pos[0], self._player_grid_pos[1]+1)
                if self._player_grid_pos[1]+1 <= MAP_SIZE-2:
                    self._player_grid_pos = new_coords
                    self._player_direction = 'Down'
                    self._view.update_frames(self._player_direction)
                    self.refresh_view(self._view.out_of_bounds(new_coords))

            elif key == "Left":
                new_coords = (
                    self._player_grid_pos[0]-1, self._player_grid_pos[1])
                if self._player_grid_pos[0]-1 >= 0:
                    self._player_grid_pos = new_coords
                    self._player_direction = 'Left'
                    self._view.update_frames(self._player_direction)
                    self.refresh_view(self._view.out_of_bounds(new_coords))

            elif key == "Right":
                new_coords = (
                    self._player_grid_pos[0]+1, self._player_grid_pos[1])
                if self._player_grid_pos[0]+1 < MAP_SIZE:
                    self._player_grid_pos = new_coords
                    self._player_direction = 'Right'
                    self._view.update_frames(self._player_direction)
                    self.refresh_view(self._view.out_of_bounds(new_coords))


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
