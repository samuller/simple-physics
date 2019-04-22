import sys
import numpy
import pygame

WIDTH = 640
HEIGHT = 480
FRAMERATE_LIMIT = 120

LEFT_CLICK = 1
MIDDLE_CLICK = 2
RIGHT_CLICK = 3
SCROLL_UP = 4
SCROLL_DOWN = 5

BALL_COLOR = (255, 128, 0)
BALL_RADIUS = 10


class PhysicsObject:

    def __init__(self, pos=(0,0), spd=(0,0)):
        self.pos = pos
        self.spd = spd


objects = [PhysicsObject((90, 90), (+1, +1))]


def draw(screen):
    color = (32, 64, 96)
    pygame.draw.rect(screen, color, pygame.Rect(0, 0, WIDTH, HEIGHT))

    for object in objects:
        pygame.draw.circle(screen, BALL_COLOR, object.pos, BALL_RADIUS)


def handle_event(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == LEFT_CLICK:
            pos = pygame.mouse.get_pos()
            objects.append(PhysicsObject(pos))
        if event.button == RIGHT_CLICK:
            pos = pygame.mouse.get_pos()
            remove_el = None
            for obj in objects:
                diff = numpy.subtract(pos, obj.pos)
                if numpy.linalg.norm(diff) <= BALL_RADIUS:
                    remove_el = obj
                    break
            if remove_el is not None:
                objects.remove(remove_el)


def draw_fps(screen, fps, font):
    fps_surface = font.render(str(fps), True, pygame.Color('white'))
    screen.blit(fps_surface, (0, 0))


def update_physics(time_diff_ms):
    for obj in objects:
        obj.pos = numpy.add(obj.pos, obj.spd)


def main_loop():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    font = pygame.font.Font(None, 30)
    pygame.display.set_caption('Simple physics')

    done = False
    while not done:
        dt_ms = clock.tick(FRAMERATE_LIMIT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                break
            handle_event(event)
        update_physics(dt_ms)

        draw(screen)
        draw_fps(screen, int(clock.get_fps()), font)
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main_loop()
