import pygame

### basic variables used throughout program

screen_width = 600
screen_height = 700
ground_floor = 500
speed = 2
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
sky_surface = pygame.image.load('graphics/Sky.png').convert()
sky_surface = pygame.transform.scale2x(sky_surface)
ground_surface = pygame.image.load('graphics/ground.png').convert()
ground_rect = ground_surface.get_rect(midright = (800, ground_floor+180))