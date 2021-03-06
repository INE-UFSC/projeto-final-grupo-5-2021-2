from tkinter import Canvas, Button, PhotoImage
from typing import Container
from GUI.Container import Container

class MainMenuContainer(Container):
    def __init__(self, main_menu):
        super().__init__(main_menu)

    def main_mission_button_click(self):
        self.main_menu.container_index = 1
        self.main_menu.main_menu_view()
    
    def quit_game_button_click(self):
        self.window.destroy()

    def settings_button_click(self):
        self.main_menu.container_index = 2
        self.main_menu.main_menu_view()

    def show_menu(self):
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
        background_image = PhotoImage(file=self.relative_to_assets("background_main_menu.png"))
        background = canvas.create_image(   400.0,
                                            300.0,
                                            image=background_image)

        #quit buttom
        quit_game_button_image = PhotoImage(file=self.relative_to_assets("quit_game_button.png"))
        quit_game_button = Button(  image=quit_game_button_image,
                                    borderwidth=0,
                                    highlightthickness=0,
                                    command=lambda: self.quit_game_button_click(),
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
        settings_button = Button(   image=settings_button_image,
                                    borderwidth=0,
                                    highlightthickness=0,
                                    command=lambda: self.settings_button_click(),
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
