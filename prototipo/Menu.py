from GUI.MainMenu import MainMenu
from GUI.MainMissionContainer import MainMissionContainer
from GUI.MainMenuContainer import MainMenuContainer
from GUI.SettingsContainer import SettingsContainer
from GUI.GameOverContainer import GameOverContainer

class Menu():
    def __init__(self):
        pass

    def create_menu(self, container_index=0):
        main_menu = MainMenu(container_index)

        main_mission_container = MainMissionContainer(main_menu)
        main_menu_container = MainMenuContainer(main_menu)
        settings_container = SettingsContainer(main_menu)
        game_over_container = GameOverContainer(main_menu)
        main_menu.container.append(main_menu_container)
        main_menu.container.append(main_mission_container)
        main_menu.container.append(settings_container)
        main_menu.container.append(game_over_container)

        main_menu.main_menu_view()
