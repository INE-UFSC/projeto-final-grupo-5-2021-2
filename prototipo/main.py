from GUI.MainMenu import MainMenu
from GUI.MainMissionContainer import MainMissionContainer
from GUI.MainMenuContainer import MainMenuContainer
from GUI.SettingsContainer import SettingsContainer

main_menu = MainMenu()

main_mission_container = MainMissionContainer(main_menu)
main_menu_container = MainMenuContainer(main_menu)
settings_container = SettingsContainer(main_menu)
main_menu.container.append(main_menu_container)
main_menu.container.append(main_mission_container)
main_menu.container.append(settings_container)

main_menu.main_menu_view()
