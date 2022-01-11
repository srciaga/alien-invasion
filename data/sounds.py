import pygame


class Sounds:
    """A class to store all game music and sfx."""

    def __init__(self):
        """Initialize the game's sounds."""
        pygame.mixer.init()

        self.bullet_sound = pygame.mixer.Sound('data/sounds/bullet.wav')
        self.alien_sound = pygame.mixer.Sound('data/sounds/explosion.wav')
        self.button_sound = pygame.mixer.Sound('data/sounds/button.wav')
        self.ship_hit_sound = pygame.mixer.Sound('data/sounds/ship_hit.wav')
        self.start_music = pygame.mixer.Sound('data/sounds/sm_01.wav')
        self.gameplay_music = pygame.mixer.Sound('data/sounds/sm_03.wav')
