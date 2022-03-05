import pygame


class KeyStatus:
    MOVE_KEYS_MAPPING = {
        pygame.K_w: pygame.K_w,
        pygame.K_UP: pygame.K_w,
        pygame.K_s: pygame.K_s,
        pygame.K_DOWN: pygame.K_s,
        pygame.K_a: pygame.K_a,
        pygame.K_LEFT: pygame.K_a,
        pygame.K_d: pygame.K_d,
        pygame.K_RIGHT: pygame.K_d,
    }

    def __init__(self):
        self._move_keys = {}

    def update(self, event_list):
        self._update_move_keys(event_list)

    def _update_move_keys(self, event_list):
        related_events = [
            event for event in event_list
            if event.type in {pygame.KEYDOWN, pygame.KEYUP}
            and event.key in self.MOVE_KEYS_MAPPING
        ]
        pressed_keys = [self.MOVE_KEYS_MAPPING[event.key] for event in related_events if event.type == pygame.KEYDOWN]
        released_keys = [self.MOVE_KEYS_MAPPING[event.key] for event in related_events if event.type == pygame.KEYUP]

        for key in pressed_keys:
            self._move_keys[key] = pygame.time.get_ticks()
        for key in released_keys:
            self._move_keys.pop(key, None)

    def get_direction(self):
        OPPOSITE = {
            pygame.K_w: pygame.K_s,
            pygame.K_s: pygame.K_w,
            pygame.K_a: pygame.K_d,
            pygame.K_d: pygame.K_a,
        }
        sorted_by_time = list(sorted(self._move_keys.items(), key=lambda x: (-x[1], x[0])))

        while sorted_by_time:
            possible_direction = sorted_by_time[0][0]
            sorted_by_time = sorted_by_time[1:]
            if OPPOSITE[possible_direction] not in self._move_keys:
                return possible_direction
            sorted_by_time = [item for item in sorted_by_time if item[0] != OPPOSITE[possible_direction]]

        return None

