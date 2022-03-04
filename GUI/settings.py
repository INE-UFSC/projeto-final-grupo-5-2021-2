from cProfile import label
from tkinter import *

mainMenu = Tk()
mainMenu.title("Settings")
mainMenu.geometry("500x300")
mainMenu.configure(background="#008")


mainMission = Label(mainMenu, text="MAIN MISSION", background="#666", foreground="#fff")
mainMission.pack()

settings = Label(mainMenu, text="SETTINGS", background="#666", foreground="#fff")
settings.pack()

leadboards = Label(mainMenu, text="LEADBOARDS", background="#666", foreground="#fff")
leadboards.pack()

mainMenu.mainloop()
