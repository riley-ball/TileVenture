import tkinter as tk
from PIL import Image, ImageTk
import glob


class LoadData(object):
    def __init__(self, *args, **kwargs):

        self._images = []
        self._load_images()

    def _load_images(self):
        for filename in glob.glob("images/terrain/*.png"):
            image = Image.open(filename)
            photo = ImageTk.PhotoImage(image)
            self._images.append(photo)

    def get_data(self):
        return self._images

    def sort_data(self):
        pass
