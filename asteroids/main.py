import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return running
        pygame.Surface.fill(screen,(0, 0, 0))  # Clear screen with black
        pygame.display.flip() 
        dt = game_clock.tick(60) / 1000  # Limit to 60 FPS and get delta time in seconds

if __name__ == "__main__":
    main()