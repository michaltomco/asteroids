import pygame

import circleshape
import constants
import logger
import random


class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, constants.LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        logger.log_event("asteroid_split")
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        

        new_angle = self.velocity.rotate(random.uniform(constants.ASTEROID_MIN_RADIUS, 50))
        first_new_asteroid = Asteroid(self.position[0], self.position[1], self.radius - constants.ASTEROID_MIN_RADIUS)
        second_new_asteroid = Asteroid(self.position[0], self.position[1], self.radius - constants.ASTEROID_MIN_RADIUS)
        
        first_new_asteroid.velocity = new_angle * 1.2	
        second_new_asteroid.velocity = -1 * new_angle * 1.2
