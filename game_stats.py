class GameStats():
    '''
    跟踪游戏的统计信息
    '''
    def __init__(self,al_settings):
        '''
        初始化统计信息
        '''
        #一开始让游戏处于非活动状态
        self.game_active = False

        self.al_settings = al_settings
        self.reset_stats()

        #在任何情况下都不应该重置最高得分
        self.high_score = 0
    def reset_stats(self):
        ''' 初始化在游戏运行期间可能改变的统计信息'''
        self.ships_left = self.al_settings.ship_limit

        self.score = 0

        self.level = 1