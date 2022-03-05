import pygame

from constants import WIDTH, HEIGHT


class Tank:
    def __init__(self):
        self.image = pygame.image.load('images/tank.png')
        self.rect = self.image.get_rect().move(WIDTH // 2, HEIGHT // 2)
        self._abs_speed = 10

    def move(self, direction_key):
        get_new_speed = {
            pygame.K_w: [0, 0] if self.rect.top <= 0 else [0, -self._abs_speed],
            pygame.K_s: [0, 0] if self.rect.bottom >= HEIGHT else [0, self._abs_speed],
            pygame.K_a: [0, 0] if self.rect.left <= 0 else [-self._abs_speed, 0],
            pygame.K_d: [0, 0] if self.rect.right >= WIDTH else [self._abs_speed, 0],
        }
        self.rect.move_ip(get_new_speed[direction_key])

    def draw_on(self, screen):
        screen.blit(self.image, self.rect)

