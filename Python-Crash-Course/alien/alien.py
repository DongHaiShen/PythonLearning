import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """单个外星人"""

    def __init__(self, game_settings, screen):
        """初始化外星人并设置其位置"""
        super(Alien, self).__init__()
        self.game_settings = game_settings
        self.screen = screen

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 外星人初始位置在左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """检测是否有外星人撞到边缘"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >=screen_rect.right:
            return True
        elif self.rect.left <=0:
            return True

    def update(self):
        """向左或向右移动外星人"""
        self.x += self.game_settings.alien_speed_factor * self.game_settings.aliens_direction
        self.rect.x = self.x

