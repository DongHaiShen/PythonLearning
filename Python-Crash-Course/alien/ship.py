import pygame


class Ship():

    def __init__(self, game_settings, screen):
        self.screen = screen
        self.game_settings = game_settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # 获取整个屏幕的外接矩形
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 飞船center属性存储小数
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_left = False
        self.moving_right = False

    def update(self):
        """根据移动标志调整飞船位置"""
        """更新的是center值"""
        if self.moving_left and self.rect.left > 0:
            self.center -= self.game_settings.ship_speed_factor
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.game_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
