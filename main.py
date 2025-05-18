import pygame
from constants import *

def main():
    pygame.init()

    timer = pygame.time.Clock()
    dt = 0
    
    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

        pygame.Surface.fill(surface, color=pygame.Color(255, 255, 255))

        pygame.display.flip()

        dt = timer.tick() / 1000

if __name__ == "__main__":
    main()