import pygame
from pygame.sprite import Group

import game_functions as gf
from button import Button
from game_stats import GameStats
from scoreboard import Scoreboard
from settings import Settings
from ship import Ship


def run_game():
    pygame.init()  # 初始化游戏并创建一个屏幕对象
    game_settings = Settings()  # 所有设置项
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))  # 屏幕大小
    pygame.display.set_caption("外星人入侵")  # 标题

    play_button = Button(game_settings, screen, "Play")
    stats = GameStats(game_settings)  # 存储游戏统计信息
    scoreboard = Scoreboard(game_settings, screen, stats)
    ship = Ship(game_settings, screen)  # 创建飞船
    bullets = Group()  # 存储子弹的编组
    aliens = Group()  # 存储外星人的编组

    gf.create_alien_group(game_settings, screen, ship, aliens)

    while True:
        gf.check_events(game_settings, screen, stats, scoreboard, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(game_settings, screen, stats, scoreboard, ship, aliens, bullets)
            gf.update_aliens(game_settings, screen, stats, scoreboard, ship, aliens, bullets)

        gf.update_screen(game_settings, screen, stats, scoreboard, ship, aliens, bullets, play_button)


run_game()
