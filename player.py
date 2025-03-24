class Player:
    def __init__(self):
        # Sprite properties
        self.IMG = 0
        self.U = 0
        self.V = 0
        self.WIDTH = 16
        self.HEIGHT = 16
        
        # Movement properties
        self.DX = 2
        self.facing_right = True
        
        # Position
        self.x = 80
        self.y = 60

    def move_left(self):
        self.x -= self.DX
        self.facing_right = False

    def move_right(self):
        self.x += self.DX
        self.facing_right = True

    def move_up(self):
        self.y -= self.DX

    def move_down(self):
        self.y += self.DX
