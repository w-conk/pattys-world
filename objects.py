import pygame
import random

class Barf:
    def __init__(self):
        # Load the barf sprite
        self.image = pygame.image.load("assets/patty.png").convert_alpha()
        self.width = 6
        self.height = 6
        self.x = 0
        self.y = 0
        # Create a rect for collision detection
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def update(self):
        # Update the collision rect to match position
        self.rect.x = self.x
        self.rect.y = self.y
        
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

class Cockroach:
    def __init__(self, x, y, scale=0.5):
        # Load the cockroach sprite
        self.original_image = pygame.image.load("assets/patty.png").convert_alpha()
        self.scale = scale
        
        # Scale the image
        new_width = int(16 * scale)  # Assuming original is 16x16
        new_height = int(16 * scale)
        self.image = pygame.transform.scale(self.original_image, (new_width, new_height))
        
        # Position
        self.x = x
        self.y = y
        
        # Size properties
        self.width = new_width
        self.height = new_height
        
        # Create a rect for collision detection
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def update(self):
        # Update the collision rect to match position
        self.rect.x = self.x
        self.rect.y = self.y
        
    def move_random(self):
        # Move randomly
        self.x += random.randint(-2, 2)
        self.y += random.randint(-2, 2)
        self.update()
        
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

class Splat:
    def __init__(self):
        # Load the splat sprite
        self.image = pygame.image.load("assets/patty.png").convert_alpha()
        self.width = 16
        self.height = 16
        self.x = 0
        self.y = 0
        # Create a rect for collision detection
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def update(self):
        # Update the collision rect to match position
        self.rect.x = self.x
        self.rect.y = self.y
        
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


    