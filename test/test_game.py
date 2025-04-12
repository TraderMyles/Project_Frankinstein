from src.main import *
from src.settings import *
from src.support import *
from src.monster import *
import pytest
import pygame
import time 

class TestMain:
    def test_display_initialisation(self):
        assert not pygame.display.get_init()  # Should be False before init
        pygame.display.init()
        assert pygame.display.get_init()      # Should be True after init
        pygame.display.quit()
        assert not pygame.display.get_init()  # Should be False after quit

    def test_monster_added_to_sprites(self):
        pygame.init()
        game = Game()

        sprites = list(game.all_sprites)

        assert game.monster in game.all_sprites

        pygame.quit()

    def test_monster_name_correct(self):
        pygame.init()
        game = Game()

        assert game.monster.name == 'Sparchu'

        pygame.quit()


    def test_monster_position_on_screen(self):
        pygame.init()
        game = Game()

        monster_rect = game.monster.rect
        screen_rect = game.display_surface.get_rect()

        assert screen_rect.contains(monster_rect), "Monster is not fully within the screen bounds"

        pygame.quit()
