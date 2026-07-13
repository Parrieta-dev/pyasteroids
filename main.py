import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock() # More info at https://www.pygame.org/docs/ref/pygame.html?highlight=init#pygame.init
    dt = 0.0

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    player = Player(x = SCREEN_WIDTH/2, y= SCREEN_HEIGHT/2)

    # Game loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.update(dt)
        player.draw(screen)
        pygame.display.flip() # Refreshes the screen with the new frame
        dt = clock.tick(60) / 1000.0  # Limit to 60 FPS and get delta time in seconds

if __name__ == "__main__":
    main()
