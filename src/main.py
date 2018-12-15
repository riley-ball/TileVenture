import tkinter as tk

from model import GameModel, MAP_SIZE, START_POS
from view import GameView
from edit import EditView


# class Player(object):
#     def __init__(self, x, y):

#         self._pos = x, y

#     def move_character(x, y):
#         self._pos


class GameApp(object):
    """Top-level GUI application for TileVenture game"""

    # All private attributes
    _current_event = None
    _player_grid_pos = None
    _player_direction = None
    _edit_mode = None
    _cell_pos = None

    _master = None
    _game_view = None
    _game = None

    def __init__(self, master):
        """Construct TileVenture game in root window

        Arguments:
            master {tk.Tk} -- Window to place the game into
        """

        self._master = master
        self._game_view = None
        self._game = game = GameModel()

        self._canvas = None

        self._show_gui()
        self._setup_game()
        self._cell_pos = 5
        self.refresh_game_view()

        # Enables character movement
        self._current_event = None
        self._edit_mode = False
        self.refresh_character()

        # view.bind_all("<Key>", self._key_press)
        self._game_view.bind_all("<KeyPress>", self._keydown)
        self._game_view.bind_all("<KeyRelease>", self._keyup)

    def _show_gui(self):
        # Game canvas
        canvas_frame = tk.Canvas(self._master, bg="black")
        canvas_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        self._game_view = game_view = GameView(canvas_frame, size=self._game.grid.cells,
                                               cell_size=self._game.grid.cell_size,
                                               bg='#1F1F1F')
        self._game_view.pack()

        # Test button
        edit_frame = tk.Frame(
            self._master, highlightthickness=1, highlightbackground="black")
        edit_frame.pack(side=tk.RIGHT, fill=tk.Y)

        # Edit button
        edit_button = tk.Button(edit_frame, text="Edit Mode",
                                command=self._toggle_edit)
        edit_button.grid(row=0, column=0, pady=10)

        self._edit_view = edit_view = EditView(edit_frame, bg='#1F1F1F')
        self._edit_view.grid(row=1, column=0)

    def _setup_game(self):
        self._game_view.generate_map()
        self._player_grid_pos = START_POS
        self._player_direction = 'Down'

    def refresh_game_view(self):
        self._game_view.draw_terrain(self._player_grid_pos, self._cell_pos)
        self._game_view.draw_player(self._player_grid_pos,
                                    self._player_direction, self._cell_pos)

    def _keyup(self, event):
        self._current_event = None

    def _keydown(self, event):
        self._current_event = event

    def _toggle_edit(self):
        self._edit_mode = not self._edit_mode
        if self._edit_mode:
            self._game_view.reset_game()
            self._game_view.draw_borders(
                self._game.grid.get_border_coordinates())
        else:
            self._game_view.reset_edit()
            self.refresh_game_view()

    def refresh_character(self):
        if self._current_event != None and not self._edit_mode:
            key = self._current_event.keysym
            if key == "Up":
                new_coords = (
                    self._player_grid_pos[0], self._player_grid_pos[1]-1)
                if self._player_grid_pos[1]-1 >= 0:
                    self._player_grid_pos = new_coords
                    self._player_direction = 'Up'
                    self._game_view.update_frames(self._player_direction)
                    self._cell_pos = self._game_view.out_of_bounds(new_coords)

            elif key == "Down":
                new_coords = (
                    self._player_grid_pos[0], self._player_grid_pos[1]+1)
                if self._player_grid_pos[1]+1 <= MAP_SIZE-2:
                    self._player_grid_pos = new_coords
                    self._player_direction = 'Down'
                    self._game_view.update_frames(self._player_direction)
                    self._cell_pos = self._game_view.out_of_bounds(new_coords)

            elif key == "Left":
                new_coords = (
                    self._player_grid_pos[0]-1, self._player_grid_pos[1])
                if self._player_grid_pos[0]-1 >= 0:
                    self._player_grid_pos = new_coords
                    self._player_direction = 'Left'
                    self._game_view.update_frames(self._player_direction)
                    self._cell_pos = self._game_view.out_of_bounds(new_coords)

            elif key == "Right":
                new_coords = (
                    self._player_grid_pos[0]+1, self._player_grid_pos[1])
                if self._player_grid_pos[0]+1 < MAP_SIZE:
                    self._player_grid_pos = new_coords
                    self._player_direction = 'Right'
                    self._game_view.update_frames(self._player_direction)
                    self._cell_pos = self._game_view.out_of_bounds(new_coords)
            self.refresh_game_view()
        self._master.after(35, self.refresh_character)


def main():
    root = tk.Tk()
    game = GameApp(root)
    root.title("TileVenture")
    root.lift()
    root.attributes('-topmost', True)
    root.after_idle(root.attributes, '-topmost', False)
    root.mainloop()


if __name__ == '__main__':
    main()
