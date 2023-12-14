import pygame
from sys import exit
from random import randint, choice
from classes import Bird, Pipe
from variables import screen_width, screen, screen_height, sky_surface, ground_floor, ground_rect, ground_surface, clock

# pygame setup
pygame.init()
pygame.display.set_caption('Flappy')
game_active = True




# class and sprite group creation
bird = pygame.sprite.GroupSingle()
bird.add(Bird())
pipe_group = pygame.sprite.Group()
pipe = Pipe()

# Timer for pipes
pipe_timer = pygame.USEREVENT + 1
pygame.time.set_timer(pipe_timer,3000)



# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pipe_timer:
                pipe_group.add(Pipe())

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface, ground_rect)
    ground_rect.x-=1.5
    if ground_rect.x <= -200:
        ground_rect.x+=200

    bird.draw(screen)
    bird.update()
    pipe_group.draw(screen)
    pipe_group.update()
    pygame.display.update()
    clock.tick(60)