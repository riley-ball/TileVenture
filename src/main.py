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


        self._setup_game()
        self.refresh_view()

        view.bind_all("<Key>", self._key_press)
        # view.bind("<Down>", self._move_down)
        # view.bind("<Left>", self._move_left)
        # view.bind("<Right>", self._move_right)

    def _setup_game(self):
        self._view.generate_map()
        self._player_grid_pos = (14, 8)
        self._player_direction = 'Down'

    def refresh_view(self):
        self._view.draw_terrain(self._player_grid_pos)
        self._view.draw_player(self._player_direction)

    def _key_press(self, event):
        key = event.keysym

        # TODO change how the view is refreshed (center around character)

        if key == "Up":
            new_coords = (self._player_grid_pos[0], self._player_grid_pos[1]-1)
            check_coords = (self._player_grid_pos[0], self._player_grid_pos[1]-9)
            # if new_coords
            if check_coords in self._view.get_map():
                self._player_grid_pos = new_coords
                self._player_direction = 'Up'
                self._view.update_frames(self._player_direction)

        elif key == "Down":
            new_coords = (self._player_grid_pos[0], self._player_grid_pos[1]+1)
            check_coords = (self._player_grid_pos[0], self._player_grid_pos[1]+10)
            if check_coords in self._view.get_map():
                self._player_grid_pos = new_coords
                self._player_direction = 'Down'
                self._view.update_frames(self._player_direction)

        elif key == "Left":
            new_coords = (self._player_grid_pos[0]-1, self._player_grid_pos[1])
            check_coords = (self._player_grid_pos[0]-15, self._player_grid_pos[1])
            if check_coords in self._view.get_map():
                self._player_grid_pos = new_coords
                self._player_direction = 'Left'
                self._view.update_frames(self._player_direction)

        elif key == "Right":
            new_coords = (self._player_grid_pos[0]+1, self._player_grid_pos[1])
            check_coords = (self._player_grid_pos[0]+16, self._player_grid_pos[1])
            if check_coords in self._view.get_map():
                self._player_grid_pos = new_coords
                self._player_direction = 'Right'
                self._view.update_frames(self._player_direction)
        self.refresh_view()

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
