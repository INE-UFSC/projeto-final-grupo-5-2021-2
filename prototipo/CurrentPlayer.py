from Slug import Slug
from PlayableCharacter import PlayableCharacter


def enter_slug(player):

    return Slug(player.rect[0], player.rect[1], player.health, player.ammo, player.grenade, player.speed)


def exit_slug(player):

    new_player = PlayableCharacter(player.rect[0], player.rect[1], player.player_speed, player.player_ammo, player.player_grenade)
    new_player.health = player.player_health
    return new_player
