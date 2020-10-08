class GameStats():
    """跟踪游戏的统计信息"""

    def __init__(self, game_settings):
        """初始化统计信息"""
        self.game_settings = game_settings
        self.reset_stats()

        self.game_active = True  # 游戏刚启动时处于活动状态

    def reset_stats(self):
        self.ships_left = self.game_settings.ship_limit
