import tkinter as tk
from PIL import Image, ImageTk
import glob


class EditView(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, **kwargs)

        self.master = master

        self._images = []
        self._load_images()

        # Scroll canvas
        frame = tk.Frame(self)
        frame.grid(row=1, column=0)

        self._canvas = tk.Canvas(
            frame, bg='#FFFFFF', scrollregion=(0, 0, 0, 9770))

        vbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
        vbar.pack(side=tk.RIGHT, fill=tk.Y)
        vbar.config(command=self._canvas.yview)

        self._canvas.config(width=200, height=500)
        self._canvas.config(yscrollcommand=vbar.set)
        self._canvas.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        self._draw_edit_shop()

    def _load_images(self):
        for filename in glob.glob("images/terrain/*.png"):
            image = Image.open(filename)
            photo = ImageTk.PhotoImage(image)
            self._images.append(photo)

    def _draw_edit_shop(self):
        image = 0
        pad = 26
        for row in range(168):
            for col in range(3):
                xcoord = 16 + (col + 1) * pad + col * 32
                ycoord = 16 + (row + 1) * pad + row * 32
                self._canvas.create_image(
                    xcoord, ycoord, image=self._images[image], tag='Terrain')
                image += 1
                if image == len(self._images):
                    return
