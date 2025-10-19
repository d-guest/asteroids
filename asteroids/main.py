import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    player = Player(x, y)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.Surface.fill(screen,(0, 0, 0))  # Clear screen with black
        for drawable in drawables:
            drawable.draw(screen)  # Draw player
        dt = game_clock.tick(60) / 1000  # Limit to 60 FPS and get delta time in seconds
        updatables.update(dt)  # Update player
        pygame.display.flip()

if __name__ == "__main__":
    main()