import tkinter as tk

from model import GameModel
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

        view.draw_borders(game.grid.get_border_coordinates())

        self._setup_game()
        self.refresh_view()

        view.bind_all("<Key>", self._key_press)
        # view.bind("<Down>", self._move_down)
        # view.bind("<Left>", self._move_left)
        # view.bind("<Right>", self._move_right)

    def _setup_game(self):
        self._player_grid_pos = (7, 4)
        self._player_direction = 'Down'
        self.flag = False

    def colour_tile(self):
        self._view.draw_tiles(self._player_grid_pos)

    def refresh_view(self):
        if self.flag:
            self.colour_tile()
        self._view.draw_player(self._player_grid_pos, self._player_direction)

    def _key_press(self, event):
        key = event.keysym

        if key == "Up":
            if self._player_grid_pos[1]-1 >= 0:
                self._player_grid_pos = (self._player_grid_pos[0], self._player_grid_pos[1]-1)
                self._player_direction = 'Up'
                self.refresh_view()
        elif key == "Down":
            if self._player_grid_pos[1]+1 <= 8:
                self._player_grid_pos = (self._player_grid_pos[0], self._player_grid_pos[1]+1)
                self._player_direction = 'Down'
                self.refresh_view()
        elif key == "Left":
            if self._player_grid_pos[0]-1 >= 0:
                self._player_grid_pos = (self._player_grid_pos[0]-1, self._player_grid_pos[1])
                self._player_direction = 'Left'
                self.refresh_view()
        elif key == "Right":
            if self._player_grid_pos[0]+1 <= 14:
                self._player_grid_pos = (self._player_grid_pos[0]+1, self._player_grid_pos[1])
                self._player_direction = 'Right'
                self.refresh_view()

def main():
    root = tk.Tk()
    root.geometry("900x540")
    game = GameApp(root)
    root.lift()
    root.attributes('-topmost', True)
    root.after_idle(root.attributes, '-topmost', False)
    root.mainloop()

if __name__ == '__main__':
    main()
