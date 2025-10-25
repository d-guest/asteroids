import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import * 
from shot import *

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
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    player = Player(x, y)
    Asteroid.containers = (updatables, drawables, asteroids)
    AsteroidField.containers = (updatables,)
    asteroid_field = AsteroidField()
    Shot.containers = (updatables, drawables, shots)

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
        
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Collision detected!")
                running = False
                print("Game Over!")
            
        for asteroid in asteroids:
            for shot in shots:
                if shot.check_collision(asteroid):
                    print("Shot hit asteroid!")
                    asteroid.split()
                    shot.kill()

        pygame.display.flip()

if __name__ == "__main__":
    main()