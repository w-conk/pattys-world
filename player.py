import pygame

class Player:
    def __init__(self):
        # Load the player sprite
        self.image = pygame.image.load("assets/player.png").convert_alpha()
        self.width = 16
        self.height = 16
        
        # Position
        self.x = 80
        self.y = 60
        
        # Movement properties
        self.dx = 2
        self.facing_right = True
        
        # Create a rect for collision detection
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def update(self):
        # Update the collision rect to match position
        self.rect.x = self.x
        self.rect.y = self.y
    
    def move_left(self):
        self.x -= self.dx
        self.facing_right = False
        self.update()

    def move_right(self):
        self.x += self.dx
        self.facing_right = True
        self.update()

    def move_up(self):
        self.y -= self.dx
        self.update()

    def move_down(self):
        self.y += self.dx
        self.update()
        
    def draw(self, screen):
        # Create a temporary surface that can be flipped
        temp_image = self.image
        
        # Flip the image if facing left
        if not self.facing_right:
            temp_image = pygame.transform.flip(self.image, True, False)
            
        # Draw the player at the current position
        screen.blit(temp_image, (self.x, self.y))
