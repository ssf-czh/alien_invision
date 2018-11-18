import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
from random import randint
def get_number_rows(al_settings, ship_height, alien_height):
    available_space_y = (al_settings.screen_height -(3 * alien_height)- ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows
def get_number_aliens_x(al_settings, alien_width):
    available_space_x = al_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x
def creat_alien(al_settings, screen, aliens ,alien_number, row_number):
    alien = Alien(al_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.y = alien.rect.height +2 * alien.rect.height *row_number
    alien.rect.x = alien.x
    aliens.add(alien)
def creat_fleet(al_settings, screen, ship, aliens):
    '''
    创建外星人群
    '''
    # 计算一行可容纳多少个外星人
    # 间距为外星人宽度
    alien = Alien(al_settings, screen)

    number_aliens_x = get_number_aliens_x(al_settings,alien.rect.width)
    number_rows = get_number_rows(al_settings, ship.rect.height ,alien.rect.height)

    # 创建第一行外星人
    for row_number in range(number_rows):
        #rand = randint(1,7)
        for alien_number in range(number_aliens_x):
            # 创建一个外星人并加入当前行
            creat_alien(al_settings,screen,aliens,alien_number,row_number)



def fire_bullet(al_settings,screen,ship,bullets):
    new_bullet = Bullet(al_settings, screen, ship)
    bullets.add(new_bullet)

def check_keydown_event(event,al_settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE :#and len(bullets) < al_settings.bullets_allowed:
        fire_bullet(al_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()
def check_keyup_event(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_play_botton(al_settings, screen, stats, sb, play_botton, ship, aliens, bullets, mouse_x,mouse_y):
    '''在玩家点击play时开始新游戏'''
    button_click = play_botton.rect.collidepoint(mouse_x,mouse_y)
    if button_click and not stats.game_active:
        pygame.mouse.set_visible(False)
        al_settings.initialize_dynamic_settings()
        #重置统计信息
        stats.reset_stats()
        stats.game_active = True
        #重置积分牌图像
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level

        sb.prep_ships()

        #清空子弹和外星人
        aliens.empty()
        bullets.empty()

        #创建新的外星人 并让飞船在中间
        creat_fleet(al_settings, screen, ship, aliens)
        ship.center_ship()


def check_events(al_settings,screen,stats,sb, play_button, ship, aliens, bullets):
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_keydown_event(event,al_settings,screen,ship,bullets)
        elif event.type==pygame.KEYUP:
            check_keyup_event(event,ship)
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y =pygame.mouse.get_pos()
            check_play_botton(al_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x,mouse_y)

def update_screen(al_settings,screen,stats, ship,aliens, bullets, play_button, sb):
    screen.fill(al_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    sb.show_score()
    #如果非活动状态，就绘制按钮
    if not stats.game_active :
        play_button.draw_button()

    pygame.display.flip()

def update_bullets(al_settings, screen, ship, aliens,bullets, stats, sb):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    #检查是否有子弹击中外星人
    #如果这样 就删除对应的子弹和外星人
    check_bullet_alien_collisions(al_settings,screen, ship, aliens, bullets, stats, sb)


def check_bullet_alien_collisions(al_settings,screen, ship, aliens, bullets, stats, sb):
    collisions = pygame.sprite.groupcollide(bullets, aliens,True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += len(aliens) * al_settings.alien_points
            sb.prep_score()
        check_high_score(stats, sb)
    if len(aliens) == 0:
        #删除现有的子弹并新建外星人
        bullets.empty()
        al_settings.increase_speed()
        #提高等级
        stats.level +=1
        sb.prep_level()
        creat_fleet(al_settings, screen, ship, aliens)
def check_high_score(stats, sb):
    '''检查是否诞生了最高的得分'''
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

def check_fleet_edges(al_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(al_settings, aliens)
            break;
def change_fleet_direction(al_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += al_settings.fleet_drop_speed
    al_settings.fleet_direction *= -1
def update_aliens(al_settings, screen, stats, sb, ship, aliens, bullets):
    check_fleet_edges(al_settings, aliens)
    aliens.update()

    #检测外星人和飞船的碰撞
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(al_settings, screen, stats, sb, ship, aliens, bullets)
    check_aliens_bottom(al_settings, stats, screen, ship, aliens, bullets,sb)
def ship_hit(al_settings, screen, stats, sb, ship, aliens, bullets):
    '''响应被外星人撞到的飞船'''
    if stats.ships_left > 0:
        stats.ships_left -= 1
        aliens.empty()
        bullets.empty()

        sb.prep_ships()
    else:
        pygame.mouse.set_visible(True)
        stats.game_active = False
    '''创建一群新的外心人，并将初始化飞船'''
    creat_fleet(al_settings,screen, ship, aliens)
    ship.center_ship()
    sleep(0.5)




def check_aliens_bottom(al_settings, stats, screen, ship, aliens, bullet, sb):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom>=screen_rect.bottom:
            ship_hit(al_settings, screen, stats, sb, ship, aliens, bullets)
            break;