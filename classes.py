import pygame
from variables import screen_width, screen, screen_height, sky_surface, ground_floor, ground_rect, ground_surface, clock, speed
### classes used throughout program

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        original_bird_image = pygame.image.load('graphics/bird/flappy.png').convert_alpha()
        original_bird_image = pygame.transform.rotozoom(original_bird_image, 0, .3)
        self.index = 0
        self.image = original_bird_image

        # Set the rect based on the image size
        self.rect = self.image.get_rect(midbottom=(screen_width // 2, 300))

        # Adjust the rect to match the size of the scaled image

        self.gravity = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.gravity = -12

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.y >= 560:
            self.rect.y = 560

    def update(self):
        self.player_input()
        self.apply_gravity()



class Pipe_bottom(pygame.sprite.Sprite):
    def __init__(self, height) -> None:
        super().__init__()
        self.bottom = pygame.image.load('graphics/pipe/pipe.png').convert_alpha()
        self.bottom = pygame.transform.rotozoom(self.bottom, 0, .4)

        self.image = self.bottom
        self.rect = self.image.get_rect(midtop = (screen_width+50, height))
    
    def destroy(self):
        if self.rect.x <= -100: 
            self.kill()#destroys the Obstacle sprite

    def update(self):
        #move the pipe to the left
        self.rect.x-=speed
        self.destroy()

class Pipe_top(pygame.sprite.Sprite):
    def __init__(self, height) -> None:
        super().__init__()
        self.top = pygame.image.load('graphics/pipe/pipe.png').convert_alpha()
        self.top = pygame.transform.rotozoom(self.top, 180, .4)

        self.image = self.top
        self.rect = self.image.get_rect(midbottom = (screen_width+50, height-210))
    
    def destroy(self):
        if self.rect.x <= -100: 
            self.kill()#destroys the Obstacle sprite

    def update(self):
        #move the pipe to the left
        self.rect.x-=speed
        #self.destroy()