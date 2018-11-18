import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
#初始化游戏并且创建一个屏幕对象
def run_game():
    pygame.init()
    #创建屏幕的尺寸
    al_settings=Settings()
    screen=pygame.display.set_mode((al_settings.screen_width,al_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")#标题
    play_button = Button(al_settings, screen, "Play")
    ship=Ship(al_settings,screen);
    #不可能是一个子弹吧 所以用编组Group 从精灵sprite引入
    bullets = Group()
    #alien = Alien(al_settings,screen)
    aliens = Group()
    gf.creat_fleet(al_settings,screen,ship,aliens)
    stats = GameStats(al_settings)
    sb = Scoreboard(al_settings, screen, stats)
    #开始游戏的循环
    while True:
        gf.check_events(al_settings, screen, stats, sb ,play_button, ship, aliens,bullets)

        if(stats.game_active):
            ship.update()
            gf.update_bullets(al_settings, screen, ship, aliens, bullets, stats, sb)
            gf.update_aliens(al_settings, screen, stats, sb, ship, aliens, bullets)
            #每次循环时填充颜色
        gf.update_screen(al_settings,screen,stats, ship, aliens, bullets, play_button, sb)

if __name__ == '__main__':
    run_game()
