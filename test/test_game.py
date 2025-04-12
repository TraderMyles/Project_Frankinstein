from src.main import *
from src.settings import *
from src.support import *
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


