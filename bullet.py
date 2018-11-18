import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self,al_settings,screen,ship):
        super().__init__()
        self.screen=screen

        #self.rect=pygame.Rect(0,0,al_settings.bullet_width,al_settings.bullet_height)
        #这里开始
        self.image = pygame.image.load("images/111.bmp")
        self.rect = self.image.get_rect()
        #这里结束

        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = al_settings.bullet_color
        self.speed_factor = al_settings.bullet_speed_factor

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y
    def draw_bullet(self):
        #在screen上以color的rect型显示
        #pygame.draw.rect(self.screen,self.color, self.rect)
        self.screen.blit(self.image, self.rect)