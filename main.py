# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main() -> None:
    print("Starting asteroids!")

    # init groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # add classes to groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable, shots)

    # debug
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # init pygame
    pygame.init()

    # create objects and variables
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    game_clock = pygame.time.Clock()
    dt = 0
    player_1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField_1 = AsteroidField()

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for object in asteroids:
            if object.checkCollision(player_1):
                print("Game over!")
                exit()
            for shot in shots:
                if object.checkCollision(shot):
                    object.kill()
        for object in updatable:
            object.update(dt)
        screen.fill((0, 0, 0))  # black
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
