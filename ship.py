import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    def __init__(self,al_settings,screen):
        '''初始化飞船并且设置 其起始位置'''
        super(Ship, self).__init__()
        self.screen=screen
        self.al_settings=al_settings
        self.image=pygame.image.load("images/ws.bmp")
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right=False
        self.moving_left=False
        self.center=float(self.rect.centerx)
        #print(type(self.center),"********************")
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.center += self.al_settings.ship_speed_factor
        if self.moving_left and self.rect.left>0:
            self.center -= self.al_settings.ship_speed_factor
        self.rect.centerx=self.center
    def center_ship(self):
        '''让飞船在屏幕上居中'''
        self.center = self.screen_rect.centerx
