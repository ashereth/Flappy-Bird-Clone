import pygame
from variables import screen_width, screen, screen_height, sky_surface, ground_floor, ground_rect, ground_surface, clock

### classes used throughout program

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        bird_1 = pygame.image.load('graphics/bird/flappy.png').convert_alpha()
        bird_1 = pygame.transform.rotozoom(bird_1, 0, 3)
        self.moving = [bird_1]
        self.index = 0
        self.image = self.moving[self.index]
        self.rect = self.image.get_rect(midbottom = (screen_width//2, 300))
        self.gravity = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -15

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.y >= ground_floor:
            self.rect.y = ground_floor

    def update(self):
        self.player_input()
        self.apply_gravity()


class Pipe(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.top = pygame.image.load('graphics/pipe/pipe.png').convert_alpha()
        self.top_rect = self.top.get_rect(midtop = (screen_width//2, 600))
        self.bottom = pygame.image.load('graphics/pipe/pipe.png').convert_alpha()
        self.bottom = pygame.transform.rotozoom(self.bottom, 180, 1)
        self.bottom_rect = self.bottom.get_rect(midbottom = (screen_width//2, 400))

    def update(self):
        #move the pipe to the left
        self.top_rect.x-=1.5
        self.bottom_rect.x-=1.5