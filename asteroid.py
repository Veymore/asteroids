from circleshape import CircleShape
from constants import *
import pygame
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        asteroid_shape = pygame.draw.circle(
            screen, (255, 255, 255), self.position, self.radius, 2
        )
        return asteroid_shape

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        spawn_obj_angle = random.uniform(20, 50)
        spawn_obj_radius = self.radius - ASTEROID_MIN_RADIUS
        spawn_obj_velocity_list = [
            self.velocity.rotate(spawn_obj_angle),
            self.velocity.rotate(-spawn_obj_angle),
        ]
        new_asteroids = []
        for velocity in spawn_obj_velocity_list:
            new_asteroid = Asteroid(self.position.x, self.position.y, spawn_obj_radius)
            new_asteroid.velocity = velocity * 1.2
            new_asteroids.append(new_asteroid)
