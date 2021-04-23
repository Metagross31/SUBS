from tkinter import *


class Window:
    def __init__(self, size_x, size_y, title, bg_colour):
        self.size_x = size_x
        self.size_y = size_y
        self.title = title
        self.bg_colour = bg_colour

        self.win = Tk()
        self.win.title(title)
        self.screen_width = self.win.winfo_screenwidth()
        self.window_position_from_right = int(round(self.screen_width * 0.02))
        self.screen_height = self.win.winfo_screenheight()
        self.window_position_from_top = int(round(self.screen_height / self.screen_width * self.screen_width * 0.02))
        self.win.geometry(str(size_x) + "x" + str(size_y) + "+" + str(self.window_position_from_right) + "+"
                          + str(self.window_position_from_top))
        self.win.configure(background=bg_colour)

    def mainloop(self):
        self.win.mainloop()
