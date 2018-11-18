import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    '''
    表示单个外星人的类
    '''

    def __init__(self, al_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.al_settings = al_settings

        # 加载外星人图像，并且设置 rect属性
        self.image = pygame.image.load("images/lbw.bmp")
        self.rect = self.image.get_rect()

        # 每个外星人开始初始化在左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 储存外星人的准确位子
        self.x = float(self.rect.x)

    #在screen上显示image物体
    def bliteme(self):
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.x >= screen_rect.right-70:
            return True
        elif self.rect.left <= 0:
            return True
    def update(self):
        '''
        向左或者向右移动外星人
        '''
        self.x += (self.al_settings.alien_speed_factor * self.al_settings.fleet_direction)
        self.rect.x = self.x
