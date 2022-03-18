from tkinter import Tk

class MainMenu():
    def __init__(self, container_index=0, container=[]):
        self.window = Tk()
        self.container = container
        self.container_index = container_index
        self.volume_holder = 0.3

        #window geometry
        width = 800
        height = 600
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        posx = int(screen_width/2 - width/2)
        posy = int(screen_height/2 - height/2)
        self.window.geometry(f"{width}x{height}+{posx}+{posy}")

        #title and icon
        self.window.title("Metal Slug")

    def main_menu_view(self):
        #window geometry
        self.container[self.container_index].show_menu()