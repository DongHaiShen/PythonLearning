class Settings():
    '''所有设置项'''

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        self.ship_speed_factor = 1.5  # 飞船移动速度
        self.ship_limit = 3  # 剩余飞船数

        # 子弹设置
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3  # 屏幕上显示的最大子弹数

        # 外星人设置
        self.alien_speed_factor = 1
        self.aliens_drop_speed = 100  # 有外星人碰到边缘时，所有外星人下降的速度
        self.aliens_direction = 1  # 1和-1表示所有外星人向右还是向左移动
