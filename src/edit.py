import tkinter as tk
from PIL import Image, ImageTk
import glob


class EditView(object):
    def __init__(self, canvas, image, x, y, click_command, * args, **kwargs):
        # super().__init__(master, **kwargs)

        self.canvas = canvas
        self._image = image
        self._x = x
        self._y = y

        self._id = self.canvas.create_image(
            x, y, image=image, tag='edit_shop')
        self.canvas.tag_bind(self._id, "<Button-1>",
                             lambda event: click_command())

    def getImage(self):
        return self._id

    def getTile(self):
        return self._image
