import numpy as np
from PIL import Image


class Canvas:
    """Object where all shapes are going to be drawn"""

    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color

        # Create a 3d numpy array of zeros
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.data[:] = self.color

    def make(self, imagepath):
        """Creates an image by using the current numpy array. Saves it as image file."""
        img = Image.fromarray(self.data, "RGB")
        img.save(imagepath)
