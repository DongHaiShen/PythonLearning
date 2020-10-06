import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    pygame.init()  # 初始化游戏并创建一个屏幕对象
    game_settings = Settings()  # 所有设置项
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))  # 屏幕大小
    pygame.display.set_caption("外星人入侵")  # 标题

    ship = Ship(game_settings, screen)  # 创建飞船
    bullets = Group()  # 存储子弹的编组

    while True:
        gf.check_events(game_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(game_settings, screen, ship, bullets)


run_game()
