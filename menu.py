from tkinter import *


root = Tk()
root.attributes("-fullscreen", True)
from os import system

class MenuGui:
    def __init__(self, master):

        def gameRun():
            """
            Button Event
            :return: 
            Quits this window, starts new game
            """
            master.destroy()
            system("python3 Space_Invaders/src/gamefile.py")

        def content(game, desc):
            """
            :param game:
            Title for game - is passed in for Title var
            :param desc:
            Description for game - is passed in for Desc var 
            :return:
            A lovely layout!
            """

            TitleFrame = Frame(master)
            TitleFrame.pack()
            TitleFrame.place(rely=.4, relx=.5)
            DescFrame = Frame(master)
            DescFrame.pack()
            DescFrame.place(rely=.45, relx=.5)
            ButtonFrame = Frame(DescFrame, height=10, width=14)
            ButtonFrame.pack(side=BOTTOM, anchor=W)

            Title = Label(TitleFrame, text=game, fg=frame_rgb)
            Title.config(font=("Courier", '38'))
            Title.place(relx=.6, rely=.4, anchor="c")
            Title.pack(side=LEFT)

            Desc = Label(DescFrame, text=desc, fg="dark gray")
            Desc.config(font=("Sans Serif", '23'))
            Desc.pack(side=RIGHT)

            trigger = Button(ButtonFrame, text="Click to Play", bd=0, fg="dark gray", command=gameRun)
            trigger.config(font=("Courier", '18'))
            trigger.pack(side=RIGHT)

        master.wm_title("Mist Game Engine")

        # Creates Frames and colors them - styling

        frame_rgb = "#%02x%02x%02x" % (0, 19, 38)
        top_frame_rgb = "#%02x%02x%02x" % (280, 280, 280)
        bottom_frame_rgb = "#%02x%02x%02x" % (166, 166, 166)

        b_frame = Frame(master, height=50, bd=1, bg=bottom_frame_rgb)
        b_frame.pack(fill=X, side=BOTTOM)

        r_frame = Frame(master, width=145, bd=1, bg=frame_rgb)
        r_frame.pack(fill=Y, side=RIGHT)

        l_frame = Frame(master, width=145, bd=1, bg=frame_rgb)
        l_frame.pack(fill=Y, side=LEFT)

        top_frame = Frame(master, height=25, bd=1, bg=top_frame_rgb)
        top_frame.pack(fill=X, side=TOP)

        # Creates a drop-down menu for settings, games, and quick access

        copyright_label = Label(b_frame, text="© Nocuta Ltd, 2017", bg=bottom_frame_rgb, fg="light gray")
        copyright_label.pack(side=LEFT)

        menu = Menu(top_frame)
        master.config(menu=menu)

        sub_menu = Menu(menu)
        menu.add_cascade(label="Games", menu=sub_menu)

        sub_menu.add_command(label="Space Invaders", command=gameRun)
        sub_menu.add_command(label="Monster Attack", command=gameRun)
        sub_menu.add_separator()
        sub_menu.add_command(label="Report Bug", command=gameRun)

        # Content Starts HERE

        title = Label(master, text="Mist Game Engine", fg=top_frame_rgb)
        title.config(font=('Courier', '44'))
        title.pack(side=RIGHT, anchor=N, padx=15, pady=15)

        #

        content("Space Invaders", "A fun retro arcade shooter - just now with boss waves!")


m = MenuGui(root)
root.mainloop()
