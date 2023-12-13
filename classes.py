import pygame

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