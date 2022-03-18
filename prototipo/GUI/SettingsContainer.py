from tkinter import Canvas, Button, PhotoImage
from GUI.Container import Container

class SettingsContainer(Container):
    def __init__(self, main_menu):
        super().__init__(main_menu)

    def volume_down_click(self):
        if self.main_menu.volume_holder > 0.1:
            self.main_menu.volume_holder -= 0.1
        else:
            print("Volume já está no minimo")

    def volume_up_click(self):
        if self.main_menu.volume_holder <= 1:
            self.main_menu.volume_holder += 0.1
        else:
            print("Volume já está no máximo")

    def go_back_button_click(self):
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

        background_settings_image = PhotoImage(file=self.relative_to_assets("background_settings.png"))
        background = canvas.create_image(   400.0,
                                            300.0,
                                            image=background_settings_image)

        controls_image = PhotoImage(file=self.relative_to_assets("controls.png"))
        controls = canvas.create_image( 245.0,
                                        220.0,
                                        image=controls_image)

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

        volume_down_image = PhotoImage(file=self.relative_to_assets("volume_down.png"))
        volume_down = Button(   image=volume_down_image,
                                borderwidth=0,
                                highlightthickness=0,
                                command=lambda: self.volume_down_click(),
                                relief="flat")
        volume_down.place(  x=136.0,
                            y=416.0,
                            width=100.0,
                            height=46.2694091796875)

        volume_up_image = PhotoImage(file=self.relative_to_assets("volume_up.png"))
        volume_up = Button( image=volume_up_image,
                            borderwidth=0,
                            highlightthickness=0,
                            command=lambda: self.volume_up_click(),
                            relief="flat")
        volume_up.place(x=255.0,
                        y=416.0,
                        width=100.0,
                        height=46.2694091796875)

        volume_label_image = PhotoImage(file=self.relative_to_assets("volume.png"))
        volume_label = canvas.create_image( 245.0,
                                            367.0,
                                            image=volume_label_image)

        self.window.resizable(False, False)
        self.window.mainloop()
