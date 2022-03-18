from tkinter import Canvas, Button, PhotoImage
from typing import Container
from GUI.Container import Container

class GameOverContainer(Container):
    def __init__(self, main_menu):
        super().__init__(main_menu)

    def main_menu_button_click(self):
        self.main_menu.container_index = 0
        self.main_menu.main_menu_view()

    def show_menu(self):
        canvas = Canvas(self.window,
                        bg = "#FFFFFF",
                        height = 600,
                        width = 800,
                        bd = 0,
                        highlightthickness = 0,
                        relief = "ridge")
        canvas.place(x = 0, y = 0)

        game_over_image = PhotoImage(file=self.relative_to_assets("game_over.png"))
        game_over = canvas.create_image(400.0,
                                        300.0,
                                        image=game_over_image)

        main_menu_button_image = PhotoImage(file=self.relative_to_assets("main_menu.png"))
        main_menu_button = Button(  image=main_menu_button_image,
                                    borderwidth=0,
                                    highlightthickness=0,
                                    command=lambda: self.main_menu_button_click(),
                                    relief="flat")

        main_menu_button.place( x=542.0,
                                y=504.0,
                                width=219.0,
                                height=59.0)

        self.window.resizable(False, False)
        self.window.mainloop()