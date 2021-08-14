class Settings:
    """存储游戏《外星人入侵》中所有设置的类"""
    def __init__(self):
        """初始化游戏设置"""

        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 750
        self.background_color = (0,191,255)

        #飞船设置
        self.ship_width = 30
        self.ship_height = 40
        self.ship_speed = 1