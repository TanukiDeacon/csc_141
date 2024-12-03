import pygame


class Background():

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        self.image = pygame.image.load('stars.png')
        self.image = pygame.transform.scale(self.image, (1800, 900))
        self.rect = self.image.get_rect()

        self.rect1 = self.rect.copy()
        self.rect2 = self.rect.copy()
        self.rect2.top = self.rect1.bottom



    def update(self):
        
        self.rect1.y += self.settings.background_scroll_speed
        self.rect2.y += self.settings.background_scroll_speed

        #self.rect1.y -= 1
        #self.rect2.y -= 1
  

        
        if self.rect1.top >= self.screen_rect.height:  
            self.rect1.bottom = self.rect2.top

        if self.rect2.top >= self.screen_rect.height:  
            self.rect2.bottom = self.rect1.top

    def blitme(self):

        self.screen.blit(self.image, self.rect1)
        self.screen.blit(self.image, self.rect2)



    