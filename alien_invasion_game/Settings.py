class Settings:
    """存储游戏《外星人入侵》中所有设置的类"""

    def __init__(self):
        """初始化游戏设置"""

        # 屏幕设置
        self.screen_width = 700
        self.screen_height = 700
        self.background_color = (0, 191, 255)

        # 飞船设置
        self.ship_width = 30
        self.ship_height = 40
        # self.ship_speed = 1.0
        self.ship_limit = 3

        # 子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        # self.bullet_speed = 1.5
        self.bullet_color = (60, 60, 60)
        # 允许当前存在的最大子弹数量
        self.bullets_allowed = 10

        # 外星人设置
        self.alien_width = 30
        self.alien_height = 30
        # self.alien_speed = 0.2
        self.fleet_drop_speed = 10.0

        # 加快游戏节奏的速度
        self.speedup_scale = 1.1
        # 外星人分数的提高速度
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # 初始化随游戏进行而变化的设置
        self.ship_speed = 1.0
        self.bullet_speed = 1.5
        self.alien_speed = 0.2
        # 计分
        self.alien_points = 50

        # fleet_direction = 1 表示向右移， = -1 表示向左移
        self.fleet_direction = 1

    def increase_speed(self):
        # 提高速度设置
        self.ship_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        # 提高外星人分数
        self.alien_points = int(self.alien_points * self.score_scale)
