import pyxel
from player import Player
from objects import Barf, Cockroach, Splat
import random

class App:
    def __init__(self):
        pyxel.init(200, 200, title="Patty's World")
        pyxel.load("PYXEL_RESOURCE_FILE.pyxres")
        
        self.player = Player()  # Center of screen
        
        # Random starting position for cockroach
        random_x = random.randint(0, 200 - 16)  # 16 is the BASE_WIDTH before scaling
        random_y = random.randint(0, 200 - 16)  # 16 is the BASE_HEIGHT before scaling
        self.cockroach = Cockroach(random_x, random_y, scale=1)
        self.score = 0
        self.splats = []  # List to store Splat objects
        
        pyxel.run(self.update, self.draw)

    def check_collision(self, rect1, rect2):
        # Check if two rectangles overlap
        return (rect1.x < rect2.x + rect2.WIDTH and
                rect1.x + rect1.WIDTH > rect2.x and
                rect1.y < rect2.y + rect2.HEIGHT and
                rect1.y + rect1.HEIGHT > rect2.y)

    def respawn_cockroach(self):
        # Create a new Splat object at cockroach's position
        new_splat = Splat()
        new_splat.x = self.cockroach.x
        new_splat.y = self.cockroach.y
        self.splats.append(new_splat)
        
        # Move cockroach to new position
        new_x = random.randint(0, 200 - self.cockroach.WIDTH)
        new_y = random.randint(0, 200 - self.cockroach.HEIGHT)
        self.cockroach.x = new_x
        self.cockroach.y = new_y

    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.player.move_left() 
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.player.move_right()
        elif pyxel.btn(pyxel.KEY_UP):
            self.player.move_up()
        elif pyxel.btn(pyxel.KEY_DOWN):
            self.player.move_down()
            
        self.cockroach.x += random.randint(-2, 2)
        self.cockroach.y += random.randint(-2, 2)
        
        self.cockroach.x = max(0, min(self.cockroach.x, 200 - self.cockroach.WIDTH))
        self.cockroach.y = max(0, min(self.cockroach.y, 200 - self.cockroach.HEIGHT))

        # Check for collision and respawn cockroach
        if self.check_collision(self.player, self.cockroach):
            self.respawn_cockroach()
            self.score += 1
            
    def draw(self):
        pyxel.cls(0)
        
        # Draw all splats first
        for splat in self.splats:
            pyxel.blt(
                splat.x,
                splat.y,
                splat.IMG,
                splat.U,
                splat.V,
                -splat.WIDTH,
                splat.HEIGHT,
                colkey=0
            )
            
        # Draw cockroach
        pyxel.blt(
            self.cockroach.x, 
            self.cockroach.y, 
            self.cockroach.IMG, 
            self.cockroach.U, 
            self.cockroach.V, 
            -self.cockroach.WIDTH,
            self.cockroach.HEIGHT,
            colkey=0
        )
        
        # Draw player with direction
        width = self.player.WIDTH if self.player.facing_right else -self.player.WIDTH
        pyxel.blt(
            self.player.x, 
            self.player.y, 
            self.player.IMG, 
            self.player.U, 
            self.player.V, 
            width,  # Will flip based on direction
            self.player.HEIGHT,
            colkey=0
        )
        
        # Draw score
        pyxel.text(5, 5, f"Score: {self.score}", 7)
        
App()