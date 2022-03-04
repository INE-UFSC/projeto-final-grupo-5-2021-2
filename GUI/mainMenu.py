from tkinter import *
from turtle import width

mainMenu = Tk()
mainMenu.title("Metal Slug Pygame")

mainMenu.geometry("600x412+500+250")
mainMenu.resizable(False,False)

# mainMenu.call('wm', 'iconphoto', mainMenu._w, PhotoImage(file='icon.png'))

def mainMissionClick():
    exec(open("prototipo/game.py").read())


def settingsClick():
    exec(open("settings.py").read())


def leadboardsClick():
    exec(open("leadboards.py").read())


# Buttons
mainMission = Button(mainMenu,
                    text="MAIN MISSION",
                    background="#666",
                    foreground="#fff",
                    width=30,
                    height=5, 
                    command=lambda: mainMissionClick())

settings = Button(mainMenu,
                  text="SETTINGS",
                  background="#666",
                  foreground="#fff",
                  width=25,
                  height=4, 
                  command=lambda: settingsClick())

leadboards = Button(mainMenu,
                    text="LEADBOARDS",
                    background="#666",
                    foreground="#fff",
                    width=25,
                    height=4, 
                    command=lambda: leadboardsClick())

#pack
mainMission.pack()
settings.pack()
leadboards.pack()

mainMenu.mainloop()
