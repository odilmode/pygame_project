from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "blue", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self,):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        
        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)
        radius1 = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, radius1)
        asteroid1.velocity = a * 1.2
        asteroid1 = Asteroid(self.position.x, self.position.y, radius1)
        asteroid1.velocity = b * 1.2
