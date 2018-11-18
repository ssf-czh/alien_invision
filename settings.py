class Settings():
    '''
    存储游戏的所有设置
    '''
    def __init__(self):
        #初始化游戏屏幕之类的

        #屏幕设置
        self.screen_width = 1400
        self.screen_height = 700
        self.bg_color = (255,255,255)
        #self.bg_color =(255,251,240)

        self.ship_speed_factor =1.5
        self.ship_limit = 3


        self.bullet_speed_factor = 2
        self.bullet_width = 100
        self.bullet_height = 15
        self.bullet_color = (60,60,60)

        self.bullets_allowed = 3


        self.alien_speed_factor = 1
        self.fleet_drop_speed = 20
        #dir 1为右 -1为左
        self.fleet_direction = 1


        #以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        #动态设置
        self.initialize_dynamic_settings()

       # print("*********",type(self.ship_speed_factor))

    def initialize_dynamic_settings(self):
        '''初始化随游戏进行而变化的设置'''
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        #fleet_direction 1为右 -1为左
        self.fleet_direction = 1

        #计分
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *=self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)