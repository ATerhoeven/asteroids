import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player

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

    #creating a player object in the middle of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        log_state()
        #processing the pygame event queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0, 0, 0))

        player.update(dt)
        player.draw(screen)

        pygame.display.flip()

        #calling the .tick() method on the clock object dividing it by 1000 and saving the value in dt
        dt = clock.tick(60) / 1000
        
    


if __name__ == "__main__":
    main()
