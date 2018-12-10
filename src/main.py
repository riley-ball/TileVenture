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
        self._game_timer = 999

        canvas_frame = tk.Canvas(master)
        canvas_frame.pack(side=tk.LEFT)

        self._view = view = GameView(canvas_frame, size=game.grid.cells,
                                     cell_size=game.grid.cell_size,
                                     bg='#1F1F1F')
        view.pack()

        self._setup_game()
        self.refresh_view(5)

        self._current_event = None

        # view.bind_all("<Key>", self._key_press)
        view.bind_all("<KeyPress>", self._keydown)
        view.bind_all("<KeyRelease>", self._keyup)
        self._key_flag = False

    def _setup_game(self):
        self._view.generate_map()
        self._player_grid_pos = START_POS
        self._player_direction = 'Down'

    def refresh_view(self, draw_flag):
        self._view.draw_terrain(self._player_grid_pos, draw_flag)
        self._view.draw_player(self._player_grid_pos,
                               self._player_direction, draw_flag)

    def _keyup(self, event):
        self._current_event = None

    def _keydown(self, event):
        self._current_event = event

    def refresh_character(self):
        if self._current_event != None:
            key = self._current_event.keysym
            if key == "Up":
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
        self._master.after(50, self.refresh_character)


def main():
    root = tk.Tk()
    root.geometry("960x576")
    game = GameApp(root)
    game.refresh_character()
    root.lift()
    root.attributes('-topmost', True)
    root.after_idle(root.attributes, '-topmost', False)
    root.mainloop()


if __name__ == '__main__':
    main()
