import sys
from time import sleep

import pygame

from alien import Alien
from bullet import Bullet


def check_keydown_events(event, game_settings, screen, ship, bullets):
    """按下按键"""
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(game_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    """松开按键"""
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False


def fire_bullet(game_settings, screen, ship, bullets):
    """如果未达到子弹数限制，则发射一颗子弹"""
    # 按空格键创建一颗子弹，并加入编组bullets中
    if len(bullets) < game_settings.bullet_allowed:
        new_bullet = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet)


def check_events(game_settings, screen, ship, bullets):
    """监听所有键盘和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(game_settings, screen, ship, aliens, bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环重新绘制屏幕
    screen.fill(game_settings.bg_color)

    # 重新绘制所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)  # 对编组aliens中的每个alien(sprite精灵)进行绘制

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(game_settings, screen, ship, aliens, bullets):
    """更新子弹位置，并删除已消失的子弹"""
    bullets.update()  # 对编组bullets中的每个bullet(sprite精灵)调用update()

    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(game_settings, screen, ship, aliens, bullets)


def check_bullet_alien_collisions(game_settings, screen, ship, aliens, bullets):
    """处理子弹和外星人的碰撞情况"""
    # 删除发生碰撞的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        # 外星人被全部消灭，则删除现有的所有子弹，并创建一个新的外星人群
        bullets.empty()
        create_alien_group(game_settings, screen, ship, aliens)


def get_number_aliens_x(game_settings, alien_width):
    """计算每行可容纳多少外星人"""
    available_space_x = game_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(game_settings, ship_height, alien_height):
    """计算屏幕可容纳多少行外星人"""
    available_space_y = game_settings.screen_height - ship_height - 3 * alien_height  # 在飞船上留出一定空白区域
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(game_settings, screen, aliens, alien_number, row_number):
    """创建一个外星人并将其放在当前行"""
    alien = Alien(game_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number

    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_alien_group(game_settings, screen, ship, aliens):
    """创建外星人群"""
    # 创建一个外星人，并计算一行可容纳多少外星人
    # 外星人间距为外星人的宽度
    alien = Alien(game_settings, screen)
    alien_width = alien.rect.width
    available_space_x = game_settings.screen_width - 2 * alien_width
    number_aliens_x = get_number_aliens_x(game_settings, alien.rect.width)
    number_rows = get_number_rows(game_settings, ship.rect.height, alien.rect.height)

    # 创建外星人群
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(game_settings, screen, aliens, alien_number, row_number)


def change_aliens_direction(game_settings, aliens):
    """将所有外星人下移，并修改移动方向"""
    for alien in aliens.sprites():
        alien.rect.y += game_settings.aliens_drop_speed
    game_settings.aliens_direction *= -1


def check_aliens_edges(game_settings, aliens):
    """有外星人碰到边缘时采取相应措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_aliens_direction(game_settings, aliens)
            break


def ship_hit(game_settings, stats, screen, ship, aliens, bullets):
    """当外星人撞到飞船后的处理"""
    if stats.ships_left > 0:
        # 飞船数减1
        stats.ships_left -= 1
    else:
        stats.game_active = False  # 游戏结束

    # 清空外星人和子弹列表
    aliens.empty()
    bullets.empty()

    # 创建新的外星人群，并将飞船放置在屏幕底端中央
    create_alien_group(game_settings, screen, ship, aliens)
    ship.center_ship()

    # 暂停
    sleep(0.5)


def check_aliens_bottom(game_settings, stats, screen, ship, aliens, bullets):
    """检查是否有外星人到达屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 类似飞船和外星人相碰撞一样处理
            ship_hit(game_settings, stats, screen, ship, aliens, bullets)
            break


def update_aliens(game_settings, stats, screen, ship, aliens, bullets):
    """检查是否有外星人位于屏幕边缘，并更新所有外星人的位置"""
    check_aliens_edges(game_settings, aliens)
    aliens.update()  # 对编组aliens中的每个alien(sprite精灵)调用update()

    # 检测外星人和飞船是否发生碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(game_settings, stats, screen, ship, aliens, bullets)

    check_aliens_bottom(game_settings, stats, screen, ship, aliens, bullets)
