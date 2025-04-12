from src.main import *
import pytest
import pygame
from game import Game  # adjust path if needed
from settings import WINDOW_WIDTH, WINDOW_HEIGHT

def test_game_initialization(mocker):
    # Mock Pygame display and init functions
    mock_set_mode = mocker.patch('pygame.display.set_mode')
    mock_set_caption = mocker.patch('pygame.display.set_caption')
    mock_init = mocker.patch('pygame.init')

    # Instantiate the game
    game = Game()

    # Assert pygame.init was called
    mock_init.assert_called_once()

    # Assert the display was set to the correct resolution
    mock_set_mode.assert_called_once_with((WINDOW_WIDTH, WINDOW_HEIGHT))

    # Assert the window title was set
    mock_set_caption.assert_called_once_with('Monster Battle')


