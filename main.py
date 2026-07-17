import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    
    #initializing pygame
    pygame.init()

    #new clock object
    clock = pygame.time.Clock()

    #Delta time initialized as float
    dt = 0.0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # create 2 empty groups to easier iterate over every object of the group 
    # in the game loop.
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # create a new empty sprite group for the asteroids
    asteroids = pygame.sprite.Group()

    # adding the Player class to the updateable and drawable groups. 
    # this needs to be done before these objects are created
    Player.containers = (updatable, drawable)

    # add the Asteroids class to the asteroids, drawable and updatable group,
    # so that every new asteroid is automatically added to these groups
    Asteroid.containers = (asteroids, updatable, drawable)

    # AsteroidField only contains the logic for spawning new asteroids, hence it is neither drawable nor
    # an asteroid but we need the logic in the update loop.
    AsteroidField.containers = (updatable)

    # create a new AsteroidField object
    asteroidfield = AsteroidField()

    # creating a player object in the middle of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        log_state()
        #processing the pygame event queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0, 0, 0))

        #update all the objects in the group updateable
        for object in updatable:
            object.update(dt)

        #draw all the objects in drawable
        for object in drawable:
            object.draw(screen)

        pygame.display.flip()

        #calling the .tick() method on the clock object dividing it by 1000 and saving the value in dt
        dt = clock.tick(60) / 1000
        
    


if __name__ == "__main__":
    main()
