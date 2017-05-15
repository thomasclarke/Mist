from tkinter import *
import random

si_win = Tk()
screen_width = si_win.winfo_screenwidth()
screen_height = si_win.winfo_screenheight()

si_win.geometry(str(screen_width) + "x" + str(screen_height))

alien_types = {
    'Boss':4,
    'General':3,
    'Lieutenant':2,
    'Private':1,
}
coord_choices = [
    (70, 70),
    (500, 70),
    (1000, 70)
]

class Enemy:

    def __init__(self, alien_type):
        try:
            self.alien_type = int(alien_type)
        except:
            self.alien_type = int(alien_types[alien_type])

        self.hp = self.alien_type * self.alien_type
        self.photo = PhotoImage(file=("img/alien"+str(self.alien_type)+".gif"))
        self.photo_display = self.photo.subsample(5,5)
        self.coords = random.choice(coord_choices)
        self.img_on = canvas.create_image(self.coords, image=self.photo_display)

    '''
    def move(self):
        if self.coords == (70,70):
            self.x = 70
            self.y = 70

            while 
    '''

canvas = Canvas(si_win)
canvas.pack(expand=1, fill='both')


enemy1 = Enemy('General')


si_win.mainloop()