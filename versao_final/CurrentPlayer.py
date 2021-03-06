from Slug import Slug
from Marco import Marco
from PlayableCharacter import PlayableCharacter

class CurrentPlayer:

    def __init__(self, player):
        self.__player = player
    

    @property
    def player(self):
        return self.__player
    
    @player.setter
    def player(self, new_player: PlayableCharacter):
        if isinstance(new_player, PlayableCharacter):
            self.__player = new_player

    def enter_slug(self):

        return Slug(self.player.rect[0], self.player.rect[1], self.player.health, self.player.ammo, self.player.grenade, self.player.speed, self.player.lives)

    def exit_slug(self):

        new_player = Marco(self.player.rect[0], self.player.rect[1], self.player.player_speed, self.player.player_ammo, self.player.player_grenade)
        new_player.health = self.player.player_health
        new_player.lives = self.player.lives
        return new_player
