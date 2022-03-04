from tkinter import *
import os

mainMenu = Tk()
mainMenu.title("Metal Slug Pygame")

mainMenu.geometry("600x412+500+250")
mainMenu.resizable(False,False)

# mainMenu.call('wm', 'iconphoto', mainMenu._w, PhotoImage(file='icon.png'))

cwd = str(os.getcwd())  # Get the current working directory (cwd)

def mainMissionClick():
    exec(open(r"%s\prototipo/game.py" % cwd).read())


def settingsClick():
    exec(open(r"%s\GUI\settings.py" % cwd).read())


def quitGameClick():
    mainMenu.destroy()


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

quitGame = Button(mainMenu,
                    text="QUIT GAME",
                    background="#666",
                    foreground="#fff",
                    width=25,
                    height=4, 
                    command=lambda: quitGameClick())

#pack
mainMission.pack()
settings.pack()
quitGame.pack()

mainMenu.mainloop()
