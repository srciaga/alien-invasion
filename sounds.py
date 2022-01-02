import pygame

pygame.mixer.init()

bullet_sound = pygame.mixer.Sound('sounds/bullet.wav')
alien_sound = pygame.mixer.Sound('sounds/explosion.wav')
button_sound = pygame.mixer.Sound('sounds/button.wav')
ship_hit_sound = pygame.mixer.Sound('sounds/ship_hit.wav')
start_music = pygame.mixer.Sound('sounds/sm_01.wav')
gameplay_music = pygame.mixer.Sound('sounds/sm_03.wav')
