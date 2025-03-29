import pygame
import random
import sys
import time
from player import Player
from objects import Barf, Cockroach, Splat

# Initialize pygame
pygame.init()
pygame.mixer.init()  # For sound effects

# Constants
GAME_WIDTH = 200  # Original game dimensions
GAME_HEIGHT = 200
SCALE_FACTOR = 3  # How much to scale up by
SCREEN_WIDTH = GAME_WIDTH * SCALE_FACTOR
SCREEN_HEIGHT = GAME_HEIGHT * SCALE_FACTOR
FPS = 60

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game_surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("Patty's World")
clock = pygame.time.Clock()

# Load sound effects
try:
    splat_sound = pygame.mixer.Sound("assets/splat.wav")
    
    # Load player sounds - add your sound files to assets folder
    player_sounds = [
        pygame.mixer.Sound("assets/player_sound1.wav"),
        pygame.mixer.Sound("assets/player_sound2.wav"),
        pygame.mixer.Sound("assets/player_sound3.wav")
    ]
except Exception as e:
    print(f"Warning: Could not load sounds. Error: {e}")
    splat_sound = None
    player_sounds = []

class Game:
    def __init__(self):
        self.player = Player()
        
        # Random starting position for cockroach
        random_x = random.randint(0, GAME_WIDTH - 16)
        random_y = random.randint(0, GAME_HEIGHT - 16)
        self.cockroach = Cockroach(random_x, random_y, scale=1)
        
        self.score = 0
        self.splats = []  # List to store Splat objects
        self.running = True
        
        # Sound timer variables
        self.last_sound_time = time.time()
        self.next_sound_delay = random.uniform(5, 15)  # Random time between 5-15 seconds
    
    def check_collision(self, rect1, rect2):
        # Use Pygame's built-in collision detection
        return rect1.colliderect(rect2)
    
    def respawn_cockroach(self):
        # Create a new Splat object at cockroach's position
        new_splat = Splat()
        new_splat.x = self.cockroach.x
        new_splat.y = self.cockroach.y
        new_splat.update()  # Update the rect
        self.splats.append(new_splat)
        
        # Play splat sound
        if splat_sound:
            splat_sound.play()
        
        # Move cockroach to new position
        new_x = random.randint(0, GAME_WIDTH - self.cockroach.width)
        new_y = random.randint(0, GAME_HEIGHT - self.cockroach.height)
        self.cockroach.x = new_x
        self.cockroach.y = new_y
        self.cockroach.update()  # Update the rect
        
        # Increment score
        self.score += 1
    
    def play_random_player_sound(self):
        # Check if we have any player sounds loaded
        if player_sounds:
            # Choose a random sound from the list
            random_sound = random.choice(player_sounds)
            random_sound.play()
            
            # Set a new random delay for the next sound
            self.next_sound_delay = random.uniform(5, 15)  # Random time between 5-15 seconds
            self.last_sound_time = time.time()
    
    def handle_events(self):
        # Process input events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
    
    def update(self):
        # Check if it's time to play a random player sound
        current_time = time.time()
        if current_time - self.last_sound_time > self.next_sound_delay:
            self.play_random_player_sound()
        
        # Handle keyboard input for player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.move_left()
            # Keep player in bounds
            self.player.x = max(0, self.player.x)
        elif keys[pygame.K_RIGHT]:
            self.player.move_right()
            # Keep player in bounds
            self.player.x = min(GAME_WIDTH - self.player.width, self.player.x)
        elif keys[pygame.K_UP]:
            self.player.move_up()
            # Keep player in bounds
            self.player.y = max(0, self.player.y)
        elif keys[pygame.K_DOWN]:
            self.player.move_down()
            # Keep player in bounds
            self.player.y = min(GAME_HEIGHT - self.player.height, self.player.y)
        
        # Random cockroach movement
        self.cockroach.x += random.randint(-2, 2)
        self.cockroach.y += random.randint(-2, 2)
        
        # Keep cockroach within screen bounds
        self.cockroach.x = max(0, min(self.cockroach.x, GAME_WIDTH - self.cockroach.width))
        self.cockroach.y = max(0, min(self.cockroach.y, GAME_HEIGHT - self.cockroach.height))
        self.cockroach.update()  # Update the rect
        
        # Check for collision between player and cockroach
        if self.check_collision(self.player.rect, self.cockroach.rect):
            self.respawn_cockroach()
    
    def draw(self):
        # Clear the game surface (not the screen)
        game_surface.fill((0, 0, 0))
        
        # Draw everything to the game surface
        for splat in self.splats:
            splat.draw(game_surface)
        
        self.cockroach.draw(game_surface)
        self.player.draw(game_surface)
        
        # Scale the game surface up to the screen
        scaled_surface = pygame.transform.scale(game_surface, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(scaled_surface, (0, 0))
        
        # Draw score directly to the screen (not the game surface)
        font = pygame.font.SysFont(None, 24)  # Larger font for screen
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        screen.blit(score_text, (15, 15))  # Position adjusted for scaled screen
        
        # Update the display
        pygame.display.flip()
    
    def run(self):
        # Main game loop
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            clock.tick(FPS)  # Maintain steady frame rate

# Start the game
if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
    sys.exit()