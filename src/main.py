import tkinter as tk

from model import GameModel, MAP_SIZE, START_POS
from view import GameView


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
    _view = None
    _game = None

    def __init__(self, master):
        """Construct TileVenture game in root window

        Arguments:
            master {tk.Tk} -- Window to place the game into
        """

        self._master = master
        self._view = None
        self._game = game = GameModel()

        self._canvas = None

        self._show_gui()
        self._setup_game()
        self._cell_pos = 5
        self.refresh_view()

        # Enables character movement
        self._current_event = None
        self._edit_mode = False
        self.refresh_character()

        # view.bind_all("<Key>", self._key_press)
        self._view.bind_all("<KeyPress>", self._keydown)
        self._view.bind_all("<KeyRelease>", self._keyup)

    def _show_gui(self):
        # Game canvas
        canvas_frame = tk.Canvas(self._master, width=960, height=576)
        canvas_frame.pack(side=tk.LEFT)

        self._view = view = GameView(canvas_frame, size=self._game.grid.cells,
                                     cell_size=self._game.grid.cell_size,
                                     bg='#1F1F1F')
        view.pack()

        # Test button
        test_frame = tk.Frame(self._master, width=200, height=576,
                              highlightthickness=1, highlightbackground="black")
        test_frame.pack(side=tk.RIGHT)
        test_frame.pack_propagate(0)

        test2_frame = tk.Frame(test_frame, relief=tk.GROOVE,
                               width=500, height=100, bd=1)
        test2_frame.pack()

        # Edit button
        test_button = tk.Button(test_frame, text="Edit Mode",
                                command=self._toggle_edit)
        test_button.pack()

        # Scroll canvas
        self._canvas = tk.Canvas(test2_frame)
        frame = tk.Frame(self._canvas)
        myscrollbar = tk.Scrollbar(
            test2_frame, orient="vertical", command=self._canvas.yview)
        self._canvas.configure(yscrollcommand=myscrollbar.set)

        myscrollbar.pack(side="right", fill="y")
        self._canvas.pack(side="left")
        self._canvas.create_window((0, 0), window=frame, anchor='nw')
        frame.bind("<Configure>", self._myfunction)
        self._data(frame)

    def _data(self, frame):
        for i in range(50):
            tk.Label(frame, text=i).grid(row=i, column=0)
            tk.Label(frame, text="my text"+str(i)).grid(row=i, column=1)
            tk.Label(frame, text="..........").grid(row=i, column=2)

    def _myfunction(self, event):
        self._canvas.configure(scrollregion=self._canvas.bbox(
            "all"), width=200, height=200)
        print("test")

    def _setup_game(self):
        self._view.generate_map()
        self._player_grid_pos = START_POS
        self._player_direction = 'Down'

    def refresh_view(self):
        self._view.draw_terrain(self._player_grid_pos, self._cell_pos)
        self._view.draw_player(self._player_grid_pos,
                               self._player_direction, self._cell_pos)

    def _keyup(self, event):
        self._current_event = None

    def _keydown(self, event):
        self._current_event = event

    def _toggle_edit(self):
        self._edit_mode = not self._edit_mode
        if self._edit_mode:
            self._view.reset_game()
            self._view.draw_borders(self._game.grid.get_border_coordinates())
        else:
            self._view.reset_edit()
            self.refresh_view()

    def refresh_character(self):
        if self._current_event != None and not self._edit_mode:
            key = self._current_event.keysym
            if key == "Up":
                new_coords = (
                    self._player_grid_pos[0], self._player_grid_pos[1]-1)
                if self._player_grid_pos[1]-1 >= 0:
                    self._player_grid_pos = new_coords
                    self._player_direction = 'Up'
                    self._view.update_frames(self._player_direction)
                    self._cell_pos = self._view.out_of_bounds(new_coords)

            elif key == "Down":
                new_coords = (
                    self._player_grid_pos[0], self._player_grid_pos[1]+1)
                if self._player_grid_pos[1]+1 <= MAP_SIZE-2:
                    self._player_grid_pos = new_coords
                    self._player_direction = 'Down'
                    self._view.update_frames(self._player_direction)
                    self._cell_pos = self._view.out_of_bounds(new_coords)

            elif key == "Left":
                new_coords = (
                    self._player_grid_pos[0]-1, self._player_grid_pos[1])
                if self._player_grid_pos[0]-1 >= 0:
                    self._player_grid_pos = new_coords
                    self._player_direction = 'Left'
                    self._view.update_frames(self._player_direction)
                    self._cell_pos = self._view.out_of_bounds(new_coords)

            elif key == "Right":
                new_coords = (
                    self._player_grid_pos[0]+1, self._player_grid_pos[1])
                if self._player_grid_pos[0]+1 < MAP_SIZE:
                    self._player_grid_pos = new_coords
                    self._player_direction = 'Right'
                    self._view.update_frames(self._player_direction)
                    self._cell_pos = self._view.out_of_bounds(new_coords)
            self.refresh_view()
        self._master.after(50, self.refresh_character)


def main():
    root = tk.Tk()
    game = GameApp(root)
    root.lift()
    root.attributes('-topmost', True)
    root.after_idle(root.attributes, '-topmost', False)
    root.mainloop()
    root.title("TileVenture")


if __name__ == '__main__':
    main()
