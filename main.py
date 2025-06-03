import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"
import pygame # type: ignore
import constants
import player

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0
    x = constants.SCREEN_WIDTH / 2
    y = constants.SCREEN_HEIGHT / 2
    ply = player.Player(x, y)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        black = [0,0,0]
        screen.fill(black)
        ply.update(dt)
        ply.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)

if __name__ == "__main__":
    main()
