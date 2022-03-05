import pygame
import sys

from constants import (
    WIDTH,
    HEIGHT,
    FPS,
)
from key_status import KeyStatus
from tank import Tank


class Game:
    def __init__(self):
        pygame.init()

        self.global_clock = pygame.time.Clock()
        self.player_tank = Tank()
        self.key_status = KeyStatus()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Fight Town') 

    def run(self):
        while True:
            self._run_main_loop()

    def _run_main_loop(self):
        # tick fps
        self.global_clock.tick(FPS)

        # handle events
        event_list = pygame.event.get()
        if any((event.type == pygame.QUIT for event in event_list)):
            pygame.quit()
            sys.exit(0)
        self.key_status.update(event_list)

        # handle game logic
        current_direction = self.key_status.get_direction()
        if current_direction:
            self.player_tank.move(current_direction)

        # draw frame
        self.screen.fill(pygame.Color('black'))
        self.player_tank.draw_on(self.screen)
        pygame.display.flip()


game = Game()
game.run()
