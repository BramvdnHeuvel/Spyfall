import time

class Clicker:
    def __init__(self):
        self.COOKIE_SCORE = 0

        self.RATS = 0            # 0.1 COOKIES PER SECOND
        self.SIJMENS = 1         # 5 COOKIES PER SECOND
        self.TANK_SHARKS = 0     # 100 COOKIES PER SECOND
        self.DEMABES = 0         # 20'000 COOKIES PER SECOND

        self.TIME = time.time()
        self.CLICK_TIME = time.time()

        self.clicks = 0
        
    def refresh_counter(self):
        print(self.clicks)
        if self.clicks > 70:
            self.punish()
        self.clicks = 0
    
    def punish(self):
        """Punish them if they're too quick!"""
        self.COOKIE_SCORE = 0

        self.RATS = 0            # 0.1 COOKIES PER SECOND
        self.SIJMENS = 0         # 5 COOKIES PER SECOND
        self.TANK_SHARKS = 0     # 100 COOKIES PER SECOND
        self.DEMABES = 0         # 2'000 COOKIES PER SECOND
        
        return f'Those abusive suckers have been PUNISHED! {self.clicks} clicks per second is WAY too much!'

    def data(self):
        return {
            'score': int(self.COOKIE_SCORE),

            'rats': self.RATS,
            'sijmens': self.SIJMENS,
            'tankSharks': self.TANK_SHARKS,
            'demabes': self.DEMABES,

            'ratPrice': int(100 * (1.25)**self.RATS),
            'sijmenPrice': int(1000 * (1.15)**self.SIJMENS),
            'tankSharkPrice': int(17000 * (1.05)**self.TANK_SHARKS),
            'demabePrice': int(654321 * (1.025)**self.DEMABES)
        }

    def click(self):
        now = time.time()
        self.clicks += 1

        if abs(now - self.CLICK_TIME) < 0.1:
            return self.data()
        
        self.COOKIE_SCORE += 1
        self.CLICK_TIME = now
        
        self.COOKIE_SCORE += abs(now - self.TIME) * (0.1*self.RATS + 5*self.SIJMENS + 100*self.TANK_SHARKS + 2000*self.DEMABES)
        self.TIME = now
        self.refresh_counter()
        return self.data()

    def buy(self, creature):
        if creature == 'nothing':
            pass
        elif creature == 'rat':
            if self.COOKIE_SCORE >= 100 * (1.25)**self.RATS:
                self.COOKIE_SCORE += -100 * (1.25)**self.RATS
                self.RATS += 1
        elif creature == 'sijmen':
            if self.COOKIE_SCORE >= 1000 * (1.15)**self.SIJMENS:
                self.COOKIE_SCORE += -1000 * (1.15)**self.SIJMENS
                self.SIJMENS += 1
        elif creature == 'tank_shark':
            if self.COOKIE_SCORE >= 17000 * (1.05)**self.TANK_SHARKS:
                self.COOKIE_SCORE += -17000 * (1.05)**self.TANK_SHARKS
                self.TANK_SHARKS += 1
        elif creature == 'demabe':
            if self.COOKIE_SCORE >= 654321 * (1.025)**self.DEMABES:
                self.COOKIE_SCORE += -654321 * (1.025)**self.DEMABES
                self.DEMABES += 1

        now = time.time()
        
        self.COOKIE_SCORE += abs(now - self.TIME) * (0.1*self.RATS + 5*self.SIJMENS + 100*self.TANK_SHARKS + 2000*self.DEMABES)
        self.TIME = now
        self.refresh_counter()

        return self.data()

cookie_object = Clicker()
clicker = cookie_object.click
buy = cookie_object.buy
ban = cookie_object.punish