from tkinter import *
from PIL import Image, ImageTk

class Display:
    '''
    passes in the image, resize value, and variable name,
    and resizes the image and assigns it to the given variable
    '''
    def resize_image(self,
                     image,
                     resize,
                     variable):
        # opens and resizes the image
        self.image = Image.open(f"assets/{image}") \
                                .resize(resize)
        self.resized_image = ImageTk.PhotoImage(self.image)
        
        # sets the variable attribute to the resized image value
        setattr(self,
                variable,
                self.resized_image)
        # returns the variable attribute
        return getattr(self, variable)