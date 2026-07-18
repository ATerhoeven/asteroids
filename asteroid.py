from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        # delete the original asteroid
        self.kill()
        # if it was large enough it will split into 2 new asteroids
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        # get a 2 new angles for the split asteroids to move towards
        random_angle = random.uniform(20, 50)
        first_asteroid_spawn_direction = self.velocity.rotate(random_angle)
        second_asteroid_spawn_direction = self.velocity.rotate(-random_angle)
        # make the new asteroids smaller
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        # create the 2 new asteroids and make them faster
        asteroid_1 = Asteroid(self.position[0], self.position[1], new_radius)
        asteroid_1.velocity = first_asteroid_spawn_direction * 1.2
        asteroid_2 = Asteroid(self.position[0], self.position[1], new_radius)
        asteroid_2.velocity = second_asteroid_spawn_direction * 1.2
