from tkinter import Canvas, Button, PhotoImage
from Mission import Mission
from GUI.Container import Container
class MainMissionContainer(Container):
    def __init__(self, main_menu):
        super().__init__(main_menu)

    def go_back_button_click(self):
        self.main_menu.container_index = 0
        self.main_menu.main_menu_view()

    def easy_button_click(self):
        mission = Mission(0, self.main_menu.volume_holder)
        self.window.destroy()
        mission.iniciar_partida()

    def show_menu(self):
        canvas = Canvas(self.window,
                        bg = "#FFFFFF",
                        height = 600,
                        width = 800,
                        bd = 0,
                        highlightthickness = 0,
                        relief = "ridge")
        canvas.place(x = 0, y = 0)

        background_image = PhotoImage(file=self.relative_to_assets("background_main_mission_menu.png"))
        background = canvas.create_image(   400.0,
                                            300.0,
                                            image=background_image)

        hard_button_image = PhotoImage(file=self.relative_to_assets("hard_button.png"))
        hard_button = Button(   image=hard_button_image,
                                borderwidth=0,
                                highlightthickness=0,
                                command=lambda: print("hard level"),
                                relief="flat")

        hard_button.place(  x=527.0,
                            y=467.0,
                            width=219.0,
                            height=59.0)

        easy_button_image = PhotoImage(file=self.relative_to_assets("easy_button.png"))
        easy_button = Button(   image=easy_button_image,
                                borderwidth=0,
                                highlightthickness=0,
                                command=lambda: self.easy_button_click(),
                                relief="flat")
        easy_button.place(  x=527.0,
                            y=253.0,
                            width=219.0,
                            height=59.0)

        medium_button_image = PhotoImage(file=self.relative_to_assets("medium_button.png"))
        medium_button = Button( image=medium_button_image,
                                borderwidth=0,
                                highlightthickness=0,
                                command=lambda: self.go_back_button_click(),
                                relief="flat")
        medium_button.place(x=527.0,
                            y=360.0,
                            width=219.0,
                            height=59.0)

        metal_slug_logo = PhotoImage(
            file=self.relative_to_assets("metal_slug_logo.png"))
        logo = canvas.create_image( 637.0,
                                    143.0,
                                    image=metal_slug_logo)

        go_back_button_image = PhotoImage(file=self.relative_to_assets("go_back_button.png"))
        go_back_button = Button(image=go_back_button_image,
                                borderwidth=0,
                                highlightthickness=0,
                                command=lambda: self.go_back_button_click(),
                                relief="flat")
        go_back_button.place(   x=34.0,
                                y=34.0,
                                width=65.0,
                                height=65.0)

        self.window.resizable(False, False)
        self.window.mainloop()