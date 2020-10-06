import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """飞船发射的子弹类"""

    def __init__(self, game_settings, screen, ship):
        """在飞船所处位置创建一个子弹对象"""
        super(Bullet, self).__init__()
        self.screen = screen

        # 在（0,0）处创建一个表示子弹的矩形，再设置到正确的位置
        self.rect = pygame.Rect(0, 0, game_settings.bullet_width, game_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 用小数表示子弹位置
        self.y = float(self.rect.y)

        self.color = game_settings.bullet_color
        self.speed_factor = game_settings.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
