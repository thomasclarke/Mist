from tkinter import *
from PIL import Image, ImageTk


print("Game Running")

mainWindow = Tk()
mainWindow.attributes("-fullscreen", True)
mainWindow.wm_title("Space Invaders")

frame_rgb = "#%02x%02x%02x" % (0, 19, 38)
r_frame = Frame(mainWindow, width=145, bd=1, bg=frame_rgb)
r_frame.pack(fill=Y, side=RIGHT)
l_frame = Frame(mainWindow, width=145, bd=1, bg=frame_rgb)
l_frame.pack(fill=Y, side=LEFT)


class Enemy:

    def __init__(self, alien_type):
        """
        :param alien_type: 
        Sets type for aliens i.e. boss
        """

        # All Aliens move
        # All aliens have images & canvases

        self.hp = alien_type*alien_type+1

        print("Alien Type %s - Health: %s" % (alien_type, self.hp))
class Alien1(Enemy):
    photo = Image.open("Space_Invaders/img/Aliens/alien1.png").resize((50, 50), Image.ANTIALIAS)
    icon = ImageTk.PhotoImage(photo)
    iconLabel = Label(image=icon)
    iconLabel.image = photo
    iconLabelDisplay = iconLabel
    iconLabelDisplay.pack()




a = Alien1
mainWindow.mainloop()
