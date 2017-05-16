from tkinter import *
import random

si_win = Tk()
screen_width = si_win.winfo_screenwidth()
screen_height = si_win.winfo_screenheight()

si_win.geometry(str(screen_width) + "x" + str(screen_height))

alien_types = [1,2,3,4]
coord_choices = [
    (70, 70),
    (500, 70),
    (1000, 70)
]

class Enemy:
    global alien_types, coord_choices
    def __init__(self, alien_type):

        self.alien_type = int(alien_type)
        self.hp = self.alien_type * self.alien_type
        self.photo = PhotoImage(file="img/alien%s.gif" % alien_type)
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

def make_enemy(alien_type):
    return Enemy(alien_type)
# CREATE ALIEN INSTANCES HERE:
def random_spawn():
    global alien_types
    alien_choice = random.choice(alien_types)
    print("Alien chosen: %s" % alien_choice)
    new_alien = make_enemy(4)
    print('Enemy spawned: Class %d, Health %d' % (new_alien.alien_type, new_alien.hp))




random_spawn()
si_win.mainloop()
