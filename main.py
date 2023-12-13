import pygame
from sys import exit
from random import randint, choice
from classes import Bird

# basic variables and pygame setup
pygame.init()
screen_width = 600
screen_height = 700
ground_floor = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy')
clock = pygame.time.Clock()
sky_surface = pygame.image.load('graphics/Sky.png').convert()
sky_surface = pygame.transform.scale2x(sky_surface)
ground_surface = pygame.image.load('graphics/ground.png').convert()
ground_rect = ground_surface.get_rect(midright = (800, ground_floor+180))




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


# class and sprite group creation
bird = pygame.sprite.GroupSingle()
bird.add(Bird())


# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface, ground_rect)
    ground_rect.x-=1.5
    print(ground_rect.x)
    if ground_rect.x <= -200:
        ground_rect.x+=200

    bird.draw(screen)
    bird.update()
    pygame.display.update()
    clock.tick(60)