import pygame


class Center():

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        self.image = pygame.image.load('media/space_center2.png')
        self.image = pygame.transform.scale(self.image, (1600, 900))
        self.rect = self.image.get_rect()




    def update(self):
       pass

    def blitme(self):

        self.screen.blit(self.image, self.rect)