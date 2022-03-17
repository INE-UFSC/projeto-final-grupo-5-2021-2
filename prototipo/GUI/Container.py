from abc import ABC
from pathlib import Path

class Container(ABC):
    def __init__(self, main_menu):
        self.main_menu = main_menu
        self.window = self.main_menu.window
        self.output_path = Path(__file__).parent
        self.assets_path = self.output_path / Path("./assets")

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)

    def show_menu(self):
        pass
