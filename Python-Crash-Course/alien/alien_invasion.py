import pygame
from pygame.sprite import Group

import game_functions as gf
from game_stats import GameStats
from settings import Settings
from ship import Ship


def run_game():
    pygame.init()  # 初始化游戏并创建一个屏幕对象
    game_settings = Settings()  # 所有设置项
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))  # 屏幕大小
    pygame.display.set_caption("外星人入侵")  # 标题

    stats = GameStats(game_settings)  # 存储游戏统计信息
    ship = Ship(game_settings, screen)  # 创建飞船
    bullets = Group()  # 存储子弹的编组
    aliens = Group()  # 存储外星人的编组

    gf.create_alien_group(game_settings, screen, ship, aliens)

    while True:
        gf.check_events(game_settings, screen, ship, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(game_settings, screen, ship, aliens, bullets)
            gf.update_aliens(game_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(game_settings, screen, ship, aliens, bullets)


run_game()
