class GameStats():
    """跟踪游戏的统计信息"""

    def __init__(self, game_settings):
        """初始化统计信息"""
        self.game_settings = game_settings
        self.reset_stats()

        self.game_active = False  # 游戏刚启动时处于非活动状态
        self.high_score = 0

    def reset_stats(self):
        self.ships_left = self.game_settings.ship_limit
        self.score = 0
        self.level = 1
