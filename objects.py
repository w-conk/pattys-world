class Barf:
    IMG = 2
    U = 0
    V = 0
    WIDTH = 6
    HEIGHT = 6

    def __init__(self):
        self.x = 0
        self.y = 0

class Cockroach:
    def __init__(self, x, y, scale=0.5):
        self.x = x
        self.y = y
        self.IMG = 1
        self.U = 0
        self.V = 0
        self.BASE_WIDTH = 16
        self.BASE_HEIGHT = 16
        self.scale = scale
        
    @property
    def WIDTH(self):
        return int(self.BASE_WIDTH * self.scale)
        
    @property
    def HEIGHT(self):
        return int(self.BASE_HEIGHT * self.scale)

class Splat:
    def __init__(self):
        self.IMG = 0
        self.U = 32
        self.V = 0
        self.WIDTH = 16
        self.HEIGHT = 16


    