import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.image = pygame.image.load('media/ship.png')
        self.image = pygame.transform.scale(self.image, (125, 115))

        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def update(self):

        if self.moving_right == True:
            self.image = pygame.image.load('media/ship_right.png')
            self.image = pygame.transform.scale(self.image, (115, 105))
        elif self.moving_left == True:
            self.image = pygame.image.load('media/ship_left.png')
            self.image = pygame.transform.scale(self.image, (115, 105))
        else:  
            self.image = pygame.image.load('media/ship.png')
            self.image = pygame.transform.scale(self.image, (125, 115))

    
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed  
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)