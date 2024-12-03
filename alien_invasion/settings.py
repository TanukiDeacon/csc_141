# this is the settings for the alien invasion game

class Settings:

    def __init__(self):

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (50,0,100)

        self.background_scroll_speed = 100
      
        self.ship_speed = 20
        self.ship_limit = 3

        self.alien_speed = 1
        self.fleet_drop_speed = 1
        self.fleet_direction = 1

        self.bullet_speed = 10.0
        self.bullet_width = 10
        self.bullet_height = 25
        self.bullet_color = (250, 0, 0)
        self.bullets_allowed = 10

        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 20
        self.bullet_speed = 10

        self.alien_speed = 1

        self.fleet_direction = 1

        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)