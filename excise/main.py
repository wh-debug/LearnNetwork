import sys
import pygame

class WinScreen:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("window")
        self.bg_color = (30, 70, 180)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            pygame.display.flip()


if __name__ == '__main__':
    win = WinScreen()
    win.run()