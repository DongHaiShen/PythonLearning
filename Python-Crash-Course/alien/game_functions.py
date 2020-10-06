import sys

import pygame

from bullet import Bullet


def check_keydown_events(event, game_settings, screen, ship, bullets):
    """按下按键"""
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(game_settings, screen, ship, bullets)


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


def update_screen(game_settings, screen, ship, bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环重新绘制屏幕
    screen.fill(game_settings.bg_color)

    # 重新绘制所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(bullets):
    """更新子弹位置，并删除已消失的子弹"""
    bullets.update()  # 对编组bullets中的每个bullet(sprite精灵)调用update()

    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
