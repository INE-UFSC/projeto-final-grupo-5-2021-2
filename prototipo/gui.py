<<<<<<< HEAD
=======

>>>>>>> a6787402ddcc0c9a2a58a2d7fb1cd800442d7519
from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
from game import Game

class MainMenu():
    def __init__(self):
        self.window = Tk()
        self.output_path = Path(__file__).parent
        self.assets_path = self.output_path / Path("./assets")

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)

    def main_mission_button_click(self):
        self.window.destroy()
        Game.iniciar_partida()

    def main_menu_view(self):

<<<<<<< HEAD
        #window geometry
        width = 800
        height = 600
        width_screen = self.window.winfo_screenwidth()
        height_screen = self.window.winfo_screenheight()
        posx = int(width_screen/2 - width/2)
        posy = int(height_screen/2 - height/2)
        self.window.geometry(f"{width}x{height}+{posx}+{posy}")

        #title and icon
        self.window.title("Metal Slug Pygame")
        icon = self.relative_to_assets('icon_marco.ico')
        self.window.iconbitmap(icon)
        #background
        self.window.configure(bg = "#FFFFFF")
=======
        #window customization 
        self.window.geometry("800x600")
        self.window.configure(bg = "#FFFFFF")

>>>>>>> a6787402ddcc0c9a2a58a2d7fb1cd800442d7519
        #canvas
        canvas = Canvas(self.window,
                        bg = "#FFFFFF",
                        height = 600,
                        width = 800,
                        bd = 0,
                        highlightthickness = 0,
                        relief = "ridge")
        canvas.place(x = 0, y = 0)

        #background
        background_image = PhotoImage(file=self.relative_to_assets("background_image.png"))
        background = canvas.create_image(   400.0,
                                            300.0,
                                            image=background_image)

        #quit buttom
        quit_game_button_image = PhotoImage(file=self.relative_to_assets("quit_game_button.png"))
        quit_game_button = Button(  image=quit_game_button_image,
                                    borderwidth=0,
                                    highlightthickness=0,
                                    command=lambda: print('oi'),
                                    relief="flat")
        quit_game_button.place( x=527.0,
                                y=467.0,
                                width=219.0,
                                height=59.0)
        
        #main mission button
        main_mission_button_image = PhotoImage(file=self.relative_to_assets("main_mission_button.png"))
        main_mission_button = Button(   image=main_mission_button_image,
                                        borderwidth=0,
                                        highlightthickness=0,
                                        command=lambda: self.main_mission_button_click(),
                                        relief="flat")
        main_mission_button.place(  x=527.0,
                                    y=253.0,
                                    width=219.0,
                                    height=59.0)

        #settings button
        settings_button_image = PhotoImage(
            file=self.relative_to_assets("settings_button.png"))
        settings_button = Button(
            image=settings_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print('aa'),
            relief="flat")
        settings_button.place(  x=527.0,
                                y=360.0,
                                width=219.0,
                                height=59.0)

        #metal slug button
        logo_image = PhotoImage(file=self.relative_to_assets("metal_slug_logo.png"))
        logo = canvas.create_image( 637.0,
                                    143.0,
                                    image=logo_image)
                                    
        self.window.resizable(False, False)
        self.window.mainloop()

main_menu = MainMenu()
<<<<<<< HEAD
main_menu.main_menu_view()
=======
main_menu.main_menu_view()
>>>>>>> a6787402ddcc0c9a2a58a2d7fb1cd800442d7519
