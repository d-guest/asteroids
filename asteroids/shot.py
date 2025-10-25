import pygame
from constants import SHOT_RADIUS
from circleshape import *

class Shot(CircleShape):
    def __init__(self, position, velocity):
        super().__init__(position.x, position.y, SHOT_RADIUS)
        self.velocity = velocity
    
    def update(self, dt):
        self.position += self.velocity * dt
        return self.position
    
    def draw(self, screen):
        return pygame.draw.circle(screen, (255, 0, 0), (int(self.position.x), int(self.position.y)), self.radius)